from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import ugettext as _

from models import Animal
from forms import AddAnimalForm


@login_required
def animal_search(request, template_name="animal/animal_search.html"):
    animals = Animal.objects.all()
    context = {'animals': animals}

    return render(request, template_name, context)


@login_required
def animal_new(request, template_name="animal/animal_new.html"):
    animal_form = AddAnimalForm(request.POST or None)

    if request.method == "POST":

        if request.POST['action'] == "save":

            if animal_form.is_valid():

                animal = animal_form.save(commit=False)
                animal.save()

                messages.success(request, _('Animal created successfully.'))
                redirect_url = reverse("animal_view", args=(animal.id,))
                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))

        else:
            messages.warning(request, _('Action not available.'))

    context = {"animal_form": animal_form,
               "creating": True}

    return render(request, template_name, context)


@login_required
def animal_view(request, animal_id, template_name="animal/animal_tabs.html"):
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

    context = {"viewing": True,
               "animal": animal,
               "animal_form": animal_form,
               "tab": "1"}

    return render(request, template_name, context)


@login_required
def animal_update(request, animal_id, template_name="animal/animal_tabs.html"):
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
               "tab": "1"}

    return render(request, template_name, context)
