import datetime
import json as simplejson

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.translation import ugettext as _

from forms import ConsultationForm, ExamForm, VaccineForm
from models import Consultation, Exam, ExamCategory, ExamType, Vaccine
from pdf import render as render_to_pdf

from animal.models import Animal
from client.models import Client
from configuration.models import Document, Image


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
def consultation_new(request, animal_id, template_name="animal/animal_tabs.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    consultation_form = ConsultationForm(request.POST or None)

    if request.method == "POST":
        if request.POST['action'] == "save":
            if consultation_form.is_valid():
                consultation = consultation_form.save(commit=False)
                consultation.animal_id = animal_id
                consultation.save()

                messages.success(request, _('Consultation created successfully.'))
                redirect_url = reverse("consultation_view", args=(consultation.service_ptr_id,))
                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))
        else:
            messages.warning(request, _('Action not available.'))

    context = {"consultation_form": consultation_form,
               "creating": True,
               "animal": animal,
               "tab": "2"}

    return render(request, template_name, context)


@login_required
def consultation_list(request, animal_id, template_name="animal/animal_tabs.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    consultation_list = Consultation.objects.filter(service_ptr_id__animal_id=animal).order_by('-date')

    if request.method == "POST":
        if request.POST['action'][:20] == "remove_consultation-":
            consultation = get_object_or_404(Consultation, pk=request.POST['action'][20:])

            try:
                consultation.delete()
                messages.success(request, _('Consultation removed successfully.'))
                redirect_url = reverse("consultation_list", args=(consultation.animal_id,))
                return HttpResponseRedirect(redirect_url)
            except ProtectedError:
                messages.error(request, _("Error trying to delete consultation."))
                redirect_url = reverse("consultation_list", args=(consultation.animal_id,))
                return HttpResponseRedirect(redirect_url)

        else:
            messages.warning(request, _('Action not available.'))

    context = {'consultation_list': consultation_list,
               'listing': True,
               'animal': animal,
               'tab': '2'}

    return render(request, template_name, context)


@login_required
def consultation_view(request, service_ptr_id, template_name="services/consultation_view_or_update.html"):
    consultation = get_object_or_404(Consultation, pk=service_ptr_id)
    consultation_form = ConsultationForm(request.POST or None, instance=consultation)
    vaccine_list = Vaccine.objects.filter(vaccine_in_consultation=consultation.pk)
    exam_list = Exam.objects.filter(exam_in_consultation=consultation.pk)

    for field in consultation_form.fields:
        consultation_form.fields[field].widget.attrs['disabled'] = True

    if request.method == "POST":
        if request.POST['action'][:15] == "remove_vaccine-":
            vaccine = get_object_or_404(Vaccine, pk=request.POST['action'][15:])
            try:
                vaccine.delete()
                messages.success(request, _('Vaccine removed successfully.'))
            except ProtectedError:
                messages.error(request, _("Error trying to delete vaccine."))

        elif request.POST['action'][:12] == "remove_exam-":
            exam = get_object_or_404(Exam, pk=request.POST['action'][12:])
            try:
                exam.delete()
                messages.success(request, _('Exam removed successfully.'))
            except ProtectedError:
                messages.error(request, _("Error trying to delete exam."))

        elif request.POST['action'][:10] == "create_pdf":
            exam = get_object_or_404(Exam, pk=request.POST['action'][11:])

            return render_to_pdf(
                'services/exam_pdf.html',
                {
                    'pagesize': 'A4',
                    'exam': exam,
                    'date': datetime.date.today(),
                    'images': Image.objects.get(),
                    'document': Document.objects.get()
                }
            )

        else:
            messages.warning(request, _('Action not available.'))

        redirect_url = reverse("consultation_view", args=(service_ptr_id,))
        return HttpResponseRedirect(redirect_url)

    context = {"viewing": True,
               "consultation": consultation,
               "consultation_form": consultation_form,
               "vaccine_list": vaccine_list,
               "exam_list": exam_list,
               "tab": "2"}

    return render(request, template_name, context)


@login_required
def consultation_update(request, service_ptr_id, template_name="services/consultation_view_or_update.html"):
    consultation = get_object_or_404(Consultation, pk=service_ptr_id)
    consultation_form = ConsultationForm(request.POST or None, instance=consultation)

    if request.method == "POST":
        if request.POST['action'] == "save":
            if consultation_form.is_valid():
                if consultation_form.has_changed():
                    consultation_form.save()
                    messages.success(request, _('Consultation updated successfully.'))
                else:
                    messages.info(request, _('There is no changes to save.'))
            else:
                messages.warning(request, _('Information not saved.'))
        else:
            messages.warning(request, _('Action not available.'))

        redirect_url = reverse("consultation_view", args=(service_ptr_id,))
        return HttpResponseRedirect(redirect_url)

    context = {"consultation": consultation,
               "consultation_form": consultation_form,
               "editing": True,
               "tab": "2"}

    return render(request, template_name, context)


@login_required
def vaccine_new(request, animal_id, service_ptr_id=None, template_name="animal/animal_tabs.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    vaccine_form = VaccineForm(request.POST or None)

    if request.method == "POST":
        if request.POST['action'] == "save":
            if vaccine_form.is_valid():
                vaccine = vaccine_form.save(commit=False)
                vaccine.animal_id = animal_id

                if service_ptr_id:
                    service = get_object_or_404(Consultation, pk=service_ptr_id)
                    vaccine.vaccine_in_consultation = service

                vaccine.save()
                messages.success(request, _('Vaccine created successfully.'))

                if service_ptr_id:
                    redirect_url = reverse("consultation_view", args=(service_ptr_id,))
                else:
                    redirect_url = reverse("vaccine_list", args=(animal.id,))

                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))

        else:
            messages.warning(request, _('Action not available.'))

    context = {"vaccine_form": vaccine_form,
               "consultation": service_ptr_id,
               "creating": True,
               "animal": animal,
               "tab": "3"}

    return render(request, template_name, context)


@login_required
def vaccine_view(request, service_ptr_id, template_name="services/vaccine_view_or_update.html"):
    vaccine = get_object_or_404(Vaccine, pk=service_ptr_id)
    vaccine_form = VaccineForm(request.POST or None, instance=vaccine)

    for field in vaccine_form.fields:
        vaccine_form.fields[field].widget.attrs['disabled'] = True

    context = {"viewing": True,
               "vaccine": vaccine,
               "vaccine_form": vaccine_form,
               "tab": "3"}

    return render(request, template_name, context)


@login_required
def vaccine_list(request, animal_id, template_name="animal/animal_tabs.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    vaccine_list = Vaccine.objects.filter(service_ptr_id__animal_id=animal).order_by('-date')

    if request.method == "POST":
        if request.POST['action'][:15] == "remove_vaccine-":
            vaccine = get_object_or_404(Vaccine, pk=request.POST['action'][15:])

            try:
                vaccine.delete()
                messages.success(request, _('Vaccine removed successfully.'))
                redirect_url = reverse("vaccine_list", args=(vaccine.animal_id,))
                return HttpResponseRedirect(redirect_url)
            except ProtectedError:
                messages.error(request, _("Error trying to delete vaccine."))
                redirect_url = reverse("vaccine_list", args=(vaccine.animal_id,))
                return HttpResponseRedirect(redirect_url)

        else:
            messages.warning(request, _('Action not available.'))

    context = {'vaccine_list': vaccine_list,
               'listing': True,
               'animal': animal,
               'tab': '3'}

    return render(request, template_name, context)


@login_required
def vaccine_update(request, service_ptr_id, template_name="services/vaccine_view_or_update.html"):
    vaccine = get_object_or_404(Vaccine, pk=service_ptr_id)
    vaccine_form = VaccineForm(request.POST or None, instance=vaccine)

    if request.method == "POST":
        if request.POST['action'] == "save":
            if vaccine_form.is_valid():
                if vaccine_form.has_changed():
                    vaccine_form.save()
                    messages.success(request, _('Vaccine updated successfully.'))
                else:
                    messages.info(request, _('There is no changes to save.'))

                if vaccine.vaccine_in_consultation:
                    redirect_url = reverse("consultation_view", args=(vaccine.vaccine_in_consultation.pk,))
                else:
                    redirect_url = reverse("vaccine_list", args=(vaccine.animal_id,))

                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))
        else:
            messages.warning(request, _('Action not available.'))

    context = {"vaccine": vaccine,
               "vaccine_form": vaccine_form,
               "editing": True,
               "tab": "3"}

    return render(request, template_name, context)


@login_required
def vaccine_booster_list(request, template_name="services/vaccine_booster_list.html"):
    vaccine_list = Vaccine.objects.filter(booster__gte=datetime.date.today()).order_by('booster')

    if request.method == "POST":
        if request.POST['action'] == "search":
            try:
                start_date = datetime.datetime.strptime(request.POST['start_date'], "%d/%m/%Y").date()
            except ValueError:
                start_date = False

            try:
                end_date = datetime.datetime.strptime(request.POST['end_date'], "%d/%m/%Y").date()
            except ValueError:
                end_date = False

            if not start_date or not end_date:
                messages.error(request, _('You must select a start date and an end date.'))

            elif end_date < start_date:
                messages.error(request, _('The end date must be greater than the start date.'))

            else:
                vaccine_list = Vaccine.objects.filter(
                    booster__gte=start_date,
                    booster__lte=end_date).order_by('booster')

    context = {"vaccine_list": vaccine_list}
    return render(request, template_name, context)


def filter_exam(request):
    if request.method == 'GET':
        category_id = request.GET.get('category')
        category = get_object_or_404(ExamCategory, id=category_id)

        exam_types = category.examtype_set.all()
        list_exam_types = []
        for a in exam_types:
            list_exam_types.append({'pk': a.id, 'valor': a.__str__()})

        json = simplejson.dumps([list_exam_types])
        return HttpResponse(json, content_type="application/json")


@login_required
def exam_new(request, animal_id, service_ptr_id=None, template_name="animal/animal_tabs.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    exam_form = ExamForm(request.POST or None)
    exams = ExamType.objects.all()

    if request.method == "POST":
        if request.POST['action'] == "save":
            if request.POST.getlist('to'):
                exam_form = ExamForm(request.POST or None, request.FILES)

                if exam_form.is_valid():
                    exam = exam_form.save(commit=False)
                    exam.animal_id = animal_id

                    if service_ptr_id:
                        service = get_object_or_404(Consultation, pk=service_ptr_id)
                        exam.exam_in_consultation = service

                    exam.save()
                    for item in request.POST.getlist('to'):
                        exam.exam_type.add(item)

                    messages.success(request, _('Exam created successfully.'))

                    if service_ptr_id:
                        redirect_url = reverse("consultation_view", args=(service_ptr_id,))
                    else:
                        redirect_url = reverse("exam_list", args=(animal.id,))

                    return HttpResponseRedirect(redirect_url)

                else:
                    messages.warning(request, _('Information not saved.'))
            else:
                messages.error(request, _('You have to select at least one exam.'))
        else:
            messages.warning(request, _('Action not available.'))

    context = {"exam_form": exam_form,
               "exams": exams,
               "consultation": service_ptr_id,
               "creating": True,
               "animal": animal,
               "tab": "4"}

    return render(request, template_name, context)


@login_required
def exam_view(request, service_ptr_id, template_name="services/exam_view_or_update.html"):
    exam = get_object_or_404(Exam, pk=service_ptr_id)
    exam_form = ExamForm(request.POST or None, instance=exam)

    for field in exam_form.fields:
        exam_form.fields[field].widget.attrs['disabled'] = True

    context = {"viewing": True,
               "exam": exam,
               "exam_form": exam_form,
               "tab": "4"}

    return render(request, template_name, context)


@login_required
def exam_list(request, animal_id, template_name="animal/animal_tabs.html"):
    animal = get_object_or_404(Animal, pk=animal_id)
    exam_list = Exam.objects.filter(service_ptr_id__animal_id=animal).order_by('-date')

    if request.method == "POST":
        if request.POST['action'][:12] == "remove_exam-":
            exam = get_object_or_404(Exam, pk=request.POST['action'][12:])

            try:
                exam.delete()
                messages.success(request, _('Exam removed successfully.'))
                redirect_url = reverse("exam_list", args=(exam.animal_id,))
                return HttpResponseRedirect(redirect_url)
            except ProtectedError:
                messages.error(request, _("Error trying to delete exam."))
                redirect_url = reverse("exam_list", args=(exam.animal_id,))
                return HttpResponseRedirect(redirect_url)

        elif request.POST['action'][:10] == "create_pdf":
            exam = get_object_or_404(Exam, pk=request.POST['action'][11:])

            return render_to_pdf(
                'services/exam_pdf.html',
                {
                    'pagesize': 'A4',
                    'exam': exam,
                    'date': datetime.date.today(),
                    'images': Image.objects.get(),
                    'document': Document.objects.get()
                }
            )

        else:
            messages.warning(request, _('Action not available.'))

    context = {'exam_list': exam_list,
               'listing': True,
               'animal': animal,
               'tab': '4'}

    return render(request, template_name, context)


@login_required
def exam_update(request, service_ptr_id, template_name="services/exam_view_or_update.html"):
    exam = get_object_or_404(Exam, pk=service_ptr_id)
    exams_selected = exam.exam_type.all()
    exams = ExamType.objects.all()
    exam_form = None

    if request.method == "POST":
        if request.POST['action'] == "save":
            if request.POST.getlist('to'):
                exam_form = ExamForm(request.POST or None, request.FILES, instance=exam)

                if exam_form.is_valid():
                    changed = False
                    if exam_form.has_changed():
                        exam_form.save()
                        changed = True

                    # Check if any examination has been deselected and remove it
                    for item in map(unicode, list(exams_selected.values_list('pk', flat=True))):
                        if item not in request.POST.getlist('to'):
                            exam.exam_type.remove(item)
                            changed = True

                    # Add selected exams
                    for item in request.POST.getlist('to'):
                        new_exam = get_object_or_404(ExamType, pk=item)
                        if new_exam not in exams_selected:
                            exam.exam_type.add(item)
                            changed = True

                    if changed:
                        messages.success(request, _('Exam updated successfully.'))
                    else:
                        messages.info(request, _('There is no changes to save.'))

                    if exam.exam_in_consultation:
                        redirect_url = reverse("consultation_view", args=(exam.exam_in_consultation.pk,))
                    else:
                        redirect_url = reverse("exam_list", args=(exam.animal_id,))

                    return HttpResponseRedirect(redirect_url)

                else:
                    messages.warning(request, _('Information not saved.'))
            else:
                messages.error(request, _('You have to select at least one exam.'))
                exam_form = ExamForm(request.POST or None, instance=exam)
        else:
            messages.warning(request, _('Action not available.'))
    else:
        exam_form = ExamForm(request.POST or None, instance=exam)

    context = {"exam": exam,
               "exams_selected": exams_selected,
               "exams": exams,
               "exam_form": exam_form,
               "editing": True,
               "tab": "4"}

    return render(request, template_name, context)
