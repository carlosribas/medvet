# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from payment.models import Payment, PaymentRegister
from payment.forms import PaymentForm, PaymentRegisterForm
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
    form = PaymentRegisterForm(request.POST or None)
    form_inlineformset = inlineformset_factory(PaymentRegister, Payment, form=PaymentForm, extra=1)
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
            payment_register = form.save(commit=False)
            payment_register.pk = None
            payment_register.installment_value = request.POST['installment_value']
            payment_register.total = request.POST['total']
            payment_register.save()

            for item in service_list:
                service = Service.objects.get(pk=item)

                if service.service_type == EXAM:
                    exam = Exam.objects.get(service_ptr_id=service.pk)
                    service.service_cost = exam.sum_exam
                    service.save()

                payment_register.service.add(item)

            payment = form_inlineformset(request.POST, instance=payment_register)
            if payment.is_valid():
                payment.save()

            messages.success(request, _('Payment registered successfully.'))
            redirect_url = reverse("client_service_list", args=(client.pk,))
            return HttpResponseRedirect(redirect_url)

        else:
            messages.warning(request, _('Information not saved.'))

    context = {
        "services": services_to_pay,
        "total": total,
        "form": form,
        "form_inlineformset": form_inlineformset,
        "client": client
    }

    return render(request, template_name, context)
