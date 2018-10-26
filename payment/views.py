# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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


def list_of_services_to_pay(service_list):
    services_to_pay = []
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

    return services_to_pay


@login_required
def payment_new(request, service_list, template_name="payment/service_payment.html"):
    service_list = [item.strip() for item in service_list.split('-')]
    services_to_pay = list_of_services_to_pay(service_list)
    total = sum(item['service_cost'] for item in services_to_pay)
    client = Service.objects.get(pk=service_list[0]).animal.owner

    form = PaymentRegisterForm(request.POST or None)
    form_inlineformset = inlineformset_factory(PaymentRegister, Payment, form=PaymentForm, extra=1)

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

                if payment_register.installment[0] == '1':
                    service.paid = 'yes'

                service.payment = payment_register
                service.save()

            payment = form_inlineformset(request.POST, instance=payment_register)
            if payment.is_valid():
                payment.save()

            messages.success(request, _('Payment registered successfully.'))
            redirect_url = reverse("client_service_list", args=(client.pk,))
            return HttpResponseRedirect(redirect_url)

        else:
            messages.warning(request, _('Information not saved.'))

    context = {
        "creating": True,
        "services": services_to_pay,
        "total": total,
        "form": form,
        "form_inlineformset": form_inlineformset,
        "client": client
    }

    return render(request, template_name, context)


@login_required
def payment_view(request, payment_id, template_name="payment/service_payment.html"):
    payment_register = get_object_or_404(PaymentRegister, pk=payment_id)
    services = Service.objects.filter(payment=payment_id)
    client = services.first().animal.owner

    payment_regiter_form = PaymentRegisterForm(instance=payment_register)
    payment_inlineformset = inlineformset_factory(PaymentRegister, Payment, form=PaymentForm, extra=0)
    payment_inlineformset = payment_inlineformset(instance=payment_register)

    for field in payment_regiter_form.fields:
        payment_regiter_form.fields[field].widget.attrs['disabled'] = True

    for form in payment_inlineformset:
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

    services_to_pay = list_of_services_to_pay(services.values_list('id', flat=True))

    context = {
        "viewing": True,
        "form": payment_regiter_form,
        "form_inlineformset": payment_inlineformset,
        "services": services_to_pay,
        "total": payment_register.total,
        "installment_value": payment_register.installment_value,
        "client": client,
        "payment_id": payment_id
    }

    return render(request, template_name, context)


@login_required
def payment_edit(request, payment_id, template_name="payment/service_payment.html"):
    payment_register = get_object_or_404(PaymentRegister, pk=payment_id)
    services = Service.objects.filter(payment=payment_id)
    client = services.first().animal.owner
    installment = int(payment_register.installment[0])

    if installment > Payment.objects.filter(payment_register=payment_register).count():
        number = 1
    else:
        number = 0

    payment_regiter_form = PaymentRegisterForm(request.POST or None, instance=payment_register)
    payment_inlineformset = inlineformset_factory(PaymentRegister, Payment, form=PaymentForm, extra=number)
    payment_inlineformset = payment_inlineformset(request.POST or None, instance=payment_register)

    for field in payment_regiter_form.fields:
        if field != 'note':
            payment_regiter_form.fields[field].widget.attrs['readonly'] = 'readonly'

    services_to_pay = list_of_services_to_pay(services.values_list('id', flat=True))

    if request.method == "POST":
        if request.POST['action'] == "save" and payment_regiter_form.is_valid():
            if payment_regiter_form.has_changed():
                payment_regiter_form.save()

            if payment_inlineformset.has_changed():
                payment_inlineformset.save()
                if installment == Payment.objects.filter(payment_register=payment_register).count():
                    for service in services:
                        service.paid = 'yes'
                        service.save()

            if payment_regiter_form.has_changed() or payment_inlineformset.has_changed():
                messages.success(request, _('Payment updated successfully.'))
            else:
                messages.warning(request, _('There is no changes to save.'))

            redirect_url = reverse("payment_view", args=(payment_id,))
            return HttpResponseRedirect(redirect_url)
        else:
            messages.warning(request, _('Information not saved.'))

    context = {
        "editing": True,
        "form": payment_regiter_form,
        "form_inlineformset": payment_inlineformset,
        "services": services_to_pay,
        "total": payment_register.total,
        "installment_value": payment_register.installment_value,
        "client": client,
        "payment_id": payment_id
    }

    return render(request, template_name, context)
