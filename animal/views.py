import json as simplejson

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import ugettext as _

from models import Specie, Animal
from forms import AddAnimalForm


def select_specie(request):
    if request.method == 'GET':
        specie_id = request.GET.get('specie')
        specie = get_object_or_404(Specie, id=specie_id)

        breeds = specie.breed_set.all()
        list_breed = []
        for a in breeds:
            list_breed.append({'pk': a.id, 'valor': a.__unicode__()})

        colors = specie.color_set.all()
        list_color = []
        for a in colors:
            list_color.append({'pk': a.id, 'valor': a.__unicode__()})

        json = simplejson.dumps([list_breed, list_color])
        return HttpResponse(json, content_type="application/json")


@login_required
def animal_record(request):
    if request.method == 'POST':
        animal = request.POST['animal']
        animal = Animal.objects.get(pk=animal)
        context = {'animal': animal, 'currentTab': '0'}
        return render(request, 'animal/animal_record.html', context)


@login_required
def add_animal(request, template_name="animal/animal_record.html"):

    animal_form = AddAnimalForm(request.POST or None)

    if request.method == "POST":

        if request.POST['action'] == "save":

            if animal_form.is_valid():

                animal = animal_form.save(commit=False)
                animal.save()

                messages.success(request, _('Animal created successfully.'))
                redirect_url = reverse("index")
                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))

        else:
            messages.warning(request, _('Action not available.'))

    context = {"animal_form": animal_form,
               "creating": True,
               "editing": True,
               "currentTab": '0'}

    return render(request, template_name, context)


@login_required
def animal_view(request, animal_id, template_name="animal/animal_record.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    animal_form = AddAnimalForm(request.POST or None, instance=animal)

    for field in animal_form.fields:
        animal_form.fields[field].widget.attrs['disabled'] = True

    if request.method == "POST":
        if request.POST['action'] == "remove":

            try:
                animal.delete()
                messages.success(request, _('Animal removed successfully.'))
                return redirect('index')
            except ProtectedError:
                messages.error(request, _("Error trying to delete animal."))
                redirect_url = reverse("animal_view", args=(animal_id,))
                return HttpResponseRedirect(redirect_url)

    context = {"can_change": True,
               "animal": animal,
               "animal_form": animal_form,
               "currentTab": '0'}

    return render(request, template_name, context)


@login_required
def animal_update(request, animal_id, template_name="animal/animal_record.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    animal_form = AddAnimalForm(request.POST or None, instance=animal)

    if request.method == "POST":
        if request.POST['action'] == "save":
            if animal_form.is_valid():
                if animal_form.has_changed():
                    animal_form.save()
                    messages.success(request, _('Animal updated successfully.'))
                else:
                    messages.success(request, _('There is no changes to save.'))

                redirect_url = reverse("animal_view", args=(animal.id,))
                return HttpResponseRedirect(redirect_url)

    context = {"animal": animal,
               "animal_form": animal_form,
               "editing": True,
               "currentTab": '0'}

    return render(request, template_name, context)
