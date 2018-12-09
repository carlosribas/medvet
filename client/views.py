from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import ugettext as _

from client.models import Client, ClientContact
from client.forms import ClientForm, ClientContactForm
from configuration.models import Page
from services.models import Service
from services.filters import ServiceFilter


@login_required
def client_new(request, template_name="client/client_new.html"):
    client_form = ClientForm(request.POST or None)
    contact_inlineformset = inlineformset_factory(Client, ClientContact, form=ClientContactForm, extra=1)

    if request.method == "POST":
        if request.POST['action'] == "save":

            if client_form.is_valid():
                client = client_form.save(commit=False)
                client.save()

                contacts = contact_inlineformset(request.POST, instance=client)
                if contacts.is_valid():
                    contacts.save()

                messages.success(request, _('Customer created successfully.'))
                redirect_url = reverse("client_view", args=(client.id,))
                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))

        else:
            messages.warning(request, _('Action not available.'))

    context = {"client_form": client_form,
               "contact_inlineformset": contact_inlineformset,
               "creating": True}

    return render(request, template_name, context)


@login_required
def client_view(request, client_id, template_name="client/client_tabs.html"):
    client = get_object_or_404(Client, pk=client_id)
    client_form = ClientForm(request.POST or None, instance=client)
    contact_inlineformset = inlineformset_factory(Client, ClientContact, form=ClientContactForm, extra=1)
    contact_inlineformset = contact_inlineformset(instance=client)

    for field in client_form.fields:
        client_form.fields[field].widget.attrs['disabled'] = True

    for form in contact_inlineformset:
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

    if request.method == "POST":
        if request.POST['action'] == "remove":

            try:
                client.delete()
                messages.success(request, _('Customer removed successfully.'))
                return redirect('client_list')
            except ProtectedError:
                messages.error(request, _("Error trying to delete the client."))
                redirect_url = reverse("client_view", args=(client_id,))
                return HttpResponseRedirect(redirect_url)

    context = {"viewing": True,
               "client": client,
               "client_form": client_form,
               "contact_inlineformset": contact_inlineformset,
               "tab": "1"
               }

    return render(request, template_name, context)


@login_required
def client_update(request, client_id, template_name="client/client_tabs.html"):
    client = get_object_or_404(Client, pk=client_id)
    client_form = ClientForm(request.POST or None, instance=client)
    contact_inlineformset = inlineformset_factory(Client, ClientContact, form=ClientContactForm, extra=1)
    contacts = contact_inlineformset(request.POST, instance=client)

    if request.method == "POST":
        if request.POST['action'] == "save":
            if client_form.is_valid() and contacts.is_valid():

                if client_form.has_changed():
                    client_form.save()

                if contacts.has_changed():
                    contacts.save()

                if client_form.has_changed() or contacts.has_changed():
                    messages.success(request, _('Customer updated successfully.'))
                else:
                    messages.warning(request, _('There is no changes to save.'))

                redirect_url = reverse("client_view", args=(client.id,))
                return HttpResponseRedirect(redirect_url)

    else:
        contact_inlineformset = contact_inlineformset(instance=client)

    context = {"client": client,
               "client_form": client_form,
               "contact_inlineformset": contact_inlineformset,
               "editing": True,
               "tab": "1"}

    return render(request, template_name, context)


@login_required
def client_list(request, template_name="client/list.html"):
    list_of_clients = Client.objects.all().order_by('name')
    page = request.GET.get('page', 1)

    try:
        get_number = Page.objects.get()
        paginator = Paginator(list_of_clients, get_number.pagination)
    except Page.DoesNotExist:
        get_number = 10
        paginator = Paginator(list_of_clients, get_number)

    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    context = {'clients': clients}

    return render(request, template_name, context)


@login_required
def client_service_list(request, client_id, template_name="client/client_tabs.html"):
    client = get_object_or_404(Client, pk=client_id)
    service_list = Service.objects.filter(animal__owner=client).order_by('-date', '-id')
    services = ServiceFilter(request.GET, queryset=service_list)

    if request.method == "POST":
        if request.POST['action'] == "pay":
            services_selected = request.POST.getlist('services')
            if not services_selected:
                messages.error(request, _('You should select at least one service'))
            else:
                services_selected = '-'.join(str(service) for service in services_selected)
                redirect_url = reverse("payment_new", args=(services_selected,))
                return HttpResponseRedirect(redirect_url)

    context = {
        "client": client,
        "services": services,
        "tab": "2"
    }

    return render(request, template_name, context)
