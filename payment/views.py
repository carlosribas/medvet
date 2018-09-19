# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from payment.forms import PaymentForm
from services.models import Service, Consultation, Vaccine, Exam, ExamName, CONSULTATION, VACCINE, EXAM
from services.filters import ServiceFilter


@login_required
def unpaid(request, template_name="payment/unpaid.html"):
    unpaid_list = Service.objects.filter(paid='no').order_by('date')
    unpaid_list = ServiceFilter(request.GET, queryset=unpaid_list)

    context = {"unpaid_list": unpaid_list}
    return render(request, template_name, context)


@login_required
def client_payment(request, service_list, template_name="payment/service_payment.html"):
    form = PaymentForm(request.POST or None)
    services_to_pay = []
    total = 0
    service_list = [item.strip() for item in service_list.split('-')]
    client = Service.objects.get(pk=service_list[0]).animal.owner

    for service in service_list:
        service = Service.objects.get(id=service)
        service_cost = 0

        if service.service_type == CONSULTATION:
            description = Consultation.objects.get(service_ptr_id=service.id)
            service_cost = description.consultation_type.price
        elif service.service_type == VACCINE:
            description = Vaccine.objects.get(service_ptr_id=service.id)
            service_cost = description.vaccine_type.price
        elif service.service_type == EXAM:
            exams = ExamName.objects.filter(exam__id=service.id)
            for exam in exams:
                service_cost += exam.price

        services_to_pay.append({
            "service_type": service.service_type,
            "service_date": service.date,
            "service_animal": service.animal.animal_name,
            "service_cost": service_cost,
        })

        total += service_cost

    if request.method == "POST":
        if request.POST['action'] == "save" and form.is_valid():
            for item in service_list:
                service = Service.objects.get(pk=item)
                payment = form.save(commit=False)
                payment.pk = None
                payment.service_id = item

                if service.service_type == EXAM:
                    exam = Exam.objects.get(service_ptr_id=service.pk)
                    payment.total = exam.sum_exam
                    service.service_cost = exam.sum_exam
                else:
                    payment.total = service.service_cost

                if item != service_list[0] or not payment.discount_or_increase:
                    payment.discount_or_increase = 0

                payment.save()
                service.paid = 'yes'
                service.save()

            messages.success(request, _('Payment registered successfully.'))
            redirect_url = reverse("client_service_list", args=(client.pk,))
            return HttpResponseRedirect(redirect_url)

        else:
            messages.warning(request, _('Information not saved.'))

    context = {"services": services_to_pay, "total": total, "form": form, "client": client}
    return render(request, template_name, context)
