import json as simplejson

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.translation import ugettext as _

from forms import ExaminationForm
from models import Examination
from animal.models import Animal
from client.models import Client


def select_animal(request):
    if request.method == 'GET':
        owner_id = request.GET.get('owner')
        owner = get_object_or_404(Client, id=owner_id)

        select = Animal.objects.filter(owner=owner)
        animal = []
        for a in select:
            animal.append({'pk': a.id, 'valor': a.__unicode__()})

        json = simplejson.dumps(animal)
        return HttpResponse(json, content_type="application/json")


@login_required
def physical_examination_new(request, animal_id, template_name="animal/animal_tabs.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    physical_examination_form = ExaminationForm(request.POST or None)

    if request.method == "POST":
        if request.POST['action'] == "save":

            if physical_examination_form.is_valid():
                physical_examination = physical_examination_form.save(commit=False)
                physical_examination.animal_id = animal_id
                physical_examination.save()

                messages.success(request, _('Physical examination created successfully.'))
                redirect_url = reverse("physical_examination_list", args=(animal.id,))
                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))

        else:
            messages.warning(request, _('Action not available.'))

    context = {"physical_examination_form": physical_examination_form,
               "creating": True,
               "animal": animal,
               "tab": "2"}

    return render(request, template_name, context)


@login_required
def physical_examination_list(request, animal_id, template_name="animal/animal_tabs.html"):
    animal = get_object_or_404(Animal, pk=animal_id)

    examination_list = Examination.objects.filter(animal_id=animal)

    context ={'examination_list': examination_list,
              'listing': True,
              'animal': animal,
              'tab': '2'}

    return render(request, template_name, context)


@login_required
def physical_examination_view(request, physical_examination_id, template_name="animal/animal_tabs.html"):
    physical_examination = get_object_or_404(Examination, pk=physical_examination_id)
    physical_examination_form = ExaminationForm(request.POST or None)

    for field in physical_examination_form.fields:
        physical_examination_form.fields[field].widget.attrs['disabled'] = True

    if request.method == "POST":
        if request.POST['action'] == "remove":

            try:
                physical_examination.delete()
                messages.success(request, _('Physical examination removed successfully.'))
                redirect_url = reverse("physical_examination_list", args=(physical_examination.animal_id,))
                return HttpResponseRedirect(redirect_url)
            except ProtectedError:
                messages.error(request, _("Error trying to delete physical examination."))
                redirect_url = reverse("physical_examination_list", args=(physical_examination.animal_id,))
                return HttpResponseRedirect(redirect_url)

    context = {"viewing": True,
               "physical_examination": physical_examination,
               "physical_examination_form": physical_examination_form,
               "tab": "2"}

    return render(request, template_name, context)


@login_required
def physical_examination_update(request, physical_examination_id, template_name="animal/animal_tabs.html"):
    physical_examination = get_object_or_404(Examination, pk=physical_examination_id)
    physical_examination_form = ExaminationForm(request.POST or None)

    if request.method == "POST":
        if request.POST['action'] == "save":
            if physical_examination_form.is_valid():
                if physical_examination_form.has_changed():
                    physical_examination_form.id = physical_examination.id
                    physical_examination_form.animal_id = physical_examination.animal_id
                    physical_examination_form.save()
                    messages.success(request, _('Physical examination updated successfully.'))
                else:
                    messages.success(request, _('There is no changes to save.'))

                redirect_url = reverse("physical_examination_view", args=(physical_examination.id,))
                return HttpResponseRedirect(redirect_url)

    context = {"physical_examination": physical_examination,
               "physical_examination_form": physical_examination_form,
               "editing": True,
               "tab": "2"}

    return render(request, template_name, context)