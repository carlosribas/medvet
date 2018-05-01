from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import ugettext as _

from models import Client, ClientContact
from forms import ClientForm


@login_required
def client_new(request, template_name="client/client.html"):
    client_form = ClientForm(request.POST or None)

    if request.method == "POST":
        if request.POST['action'] == "save":

            if client_form.is_valid():
                client = client_form.save(commit=False)
                client.save()
                messages.success(request, _('Client created successfully.'))
                redirect_url = reverse("client_view", args=(client.id,))
                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))

        else:
            messages.warning(request, _('Action not available.'))

    context = {"client_form": client_form,
               "creating": True}

    return render(request, template_name, context)


@login_required
def client_view(request, client_id, template_name="client/client.html"):
    client = get_object_or_404(Client, pk=client_id)
    client_form = ClientForm(request.POST or None, instance=client)

    for field in client_form.fields:
        client_form.fields[field].widget.attrs['disabled'] = True

    if request.method == "POST":
        if request.POST['action'] == "remove":

            try:
                client.delete()
                messages.success(request, _('Client removed successfully.'))
                return redirect('index')
            except ProtectedError:
                messages.error(request, _("Error trying to delete the client."))
                redirect_url = reverse("client_view", args=(client_id,))
                return HttpResponseRedirect(redirect_url)

    context = {"viewing": True,
               "client": client,
               "client_form": client_form}

    return render(request, template_name, context)


@login_required
def client_update(request, client_id, template_name="client/client.html"):
    client = get_object_or_404(Client, pk=client_id)
    client_form = ClientForm(request.POST or None, instance=client)

    if request.method == "POST":
        if request.POST['action'] == "save":
            if client_form.is_valid():
                if client_form.has_changed():
                    client_form.save()
                    messages.success(request, _('Client updated successfully.'))
                else:
                    messages.success(request, _('There is no changes to save.'))

                redirect_url = reverse("client_view", args=(client.id,))
                return HttpResponseRedirect(redirect_url)

    context = {"client": client,
               "client_form": client_form,
               "editing": True,
               "tab": "1"}

    return render(request, template_name, context)


@login_required
def client_search(request, template_name="client/search.html"):
    clients = Client.objects.all()

    if request.method == 'POST':
        client_id = request.POST['customer']
        if client_id != '0' and client_id != '':
            redirect_url = reverse('client_view', args=(client_id,))
            return HttpResponseRedirect(redirect_url)
        else:
            messages.warning(request, _("You should select a customer."))

    context = {'clients': clients}
    return render(request, template_name, context)
