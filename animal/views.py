import json as simplejson

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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
        context = {'animal': animal}
        return render(request, 'animal_record.html', context)


@login_required
def add_animal(request, template_name="animal/add_animal.html"):

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
               "editing": True}

    return render(request, template_name, context)


# @login_required
# @permission_required('experiment.register_equipment')
# def eegmachine_update(request, eegmachine_id, template_name="experiment/eegmachine_register.html"):
#
#     eegmachine = get_object_or_404(EEGMachine, pk=eegmachine_id)
#     # eegmachine.equipment_type = 'eeg_machine'
#
#     eegmachine_form = EEGMachineRegisterForm(request.POST or None, instance=eegmachine)
#
#     # eegmachine_form.fields['equipment_type'].widget.attrs['disabled'] = True
#
#     if request.method == "POST":
#         if request.POST['action'] == "save":
#             if eegmachine_form.is_valid():
#                 if eegmachine_form.has_changed():
#                     eegmachine_form.save()
#                     messages.success(request, _('EEG machine updated successfully.'))
#                 else:
#                     messages.success(request, _('There is no changes to save.'))
#
#                 redirect_url = reverse("eegmachine_view", args=(eegmachine.id,))
#                 return HttpResponseRedirect(redirect_url)
#
#     context = {"equipment": eegmachine,
#                "equipment_form": eegmachine_form,
#                "editing": True}
#
#     return render(request, template_name, context)
#
#
# @login_required
# @permission_required('experiment.register_equipment')
# def eegmachine_view(request, eegmachine_id, template_name="experiment/eegmachine_register.html"):
#     eegmachine = get_object_or_404(EEGMachine, pk=eegmachine_id)
#
#     eegmachine_form = EEGMachineRegisterForm(request.POST or None, instance=eegmachine)
#
#     for field in eegmachine_form.fields:
#         eegmachine_form.fields[field].widget.attrs['disabled'] = True
#
#     if request.method == "POST":
#         if request.POST['action'] == "remove":
#
#             try:
#                 eegmachine.delete()
#                 messages.success(request, _('EEG machine removed successfully.'))
#                 return redirect('eegmachine_list')
#             except ProtectedError:
#                 messages.error(request, _("Error trying to delete eegmachine."))
#                 redirect_url = reverse("eegmachine_view", args=(eegmachine_id,))
#                 return HttpResponseRedirect(redirect_url)
#
#     context = {"can_change": True,
#                "equipment": eegmachine,
#                "equipment_form": eegmachine_form}
#
#     return render(request, template_name, context)
#
