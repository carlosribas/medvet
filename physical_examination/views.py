import json as simplejson

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.translation import ugettext as _

from forms import ExaminationForm
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
def new_physical_examination(request, animal_id, template_name="animal/animal_record.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    physical_examination_form = ExaminationForm(request.POST or None)

    if request.method == "POST":

        if request.POST['action'] == "save":

            if physical_examination_form.is_valid():

                physical_examination = physical_examination_form.save(commit=False)
                physical_examination.save()

                messages.success(request, _('Physical examination created successfully.'))
                redirect_url = reverse("new_physical_examination", args=(animal.id,))
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


# @login_required
# def animal_view(request, animal_id, template_name="animal/animal_record.html"):
#     animal = get_object_or_404(Animal, pk=animal_id)
#     animal_form = AddAnimalForm(request.POST or None, instance=animal)
#
#     for field in animal_form.fields:
#         animal_form.fields[field].widget.attrs['disabled'] = True
#
#     if request.method == "POST":
#         if request.POST['action'] == "remove":
#
#             try:
#                 animal.delete()
#                 messages.success(request, _('Animal removed successfully.'))
#                 return redirect('index')
#             except ProtectedError:
#                 messages.error(request, _("Error trying to delete animal."))
#                 redirect_url = reverse("animal_view", args=(animal_id,))
#                 return HttpResponseRedirect(redirect_url)
#
#     context = {"can_change": True,
#                "animal": animal,
#                "animal_form": animal_form,
#                "tab": "1"}
#
#     return render(request, template_name, context)
#
#
# @login_required
# def animal_update(request, animal_id, template_name="animal/animal_record.html"):
#     animal = get_object_or_404(Animal, pk=animal_id)
#     animal_form = AddAnimalForm(request.POST or None, instance=animal)
#
#     if request.method == "POST":
#         if request.POST['action'] == "save":
#             if animal_form.is_valid():
#                 if animal_form.has_changed():
#                     animal_form.save()
#                     messages.success(request, _('Animal updated successfully.'))
#                 else:
#                     messages.success(request, _('There is no changes to save.'))
#
#                 redirect_url = reverse("animal_view", args=(animal.id,))
#                 return HttpResponseRedirect(redirect_url)
#
#     context = {"animal": animal,
#                "animal_form": animal_form,
#                "editing": True,
#                "tab": "1"}
#
#     return render(request, template_name, context)