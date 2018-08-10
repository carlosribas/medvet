# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from forms import PaymentForm
from services.models import Service, Consultation, Exam, Vaccine
from client.models import Client


@login_required
def unpaid(request, template_name="payment/unpaid.html"):
    unpaid_list = Service.objects.filter(paid='no').order_by('date')
    customers = Client.objects.filter(id__in=unpaid_list.values_list('animal__owner').distinct())

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

            if start_date and not end_date or not start_date and end_date:
                messages.error(request, _('You must select start date and end date.'))

            elif end_date < start_date:
                messages.error(request, _('The end date must be greater than the start date.'))

            elif not start_date and not end_date and request.POST['customer'] == '':
                messages.error(request, _('You must select start date and end date or select a customer.'))

            elif start_date and end_date and request.POST['customer'] != '':
                unpaid_list = Service.objects.filter(
                    paid='no',
                    date__gte=start_date,
                    date__lte=end_date,
                    animal__owner=request.POST['customer']
                ).order_by('date')

            elif start_date and end_date and request.POST['customer'] == '':
                unpaid_list = Service.objects.filter(
                    paid='no',
                    date__gte=start_date,
                    date__lte=end_date,
                ).order_by('date')

            elif not start_date and not end_date and request.POST['customer'] != '':
                unpaid_list = Service.objects.filter(
                    paid='no',
                    animal__owner=request.POST['customer']
                )

            else:
                messages.error(request, _('There is something wrong here!'))

    context = {"unpaid_list": unpaid_list, "customers": customers}
    return render(request, template_name, context)


@login_required
def service_payment(request, service_id, template_name="payment/service.html"):
    service = Service.objects.get(id=service_id)
    form = PaymentForm(request.POST or None)

    description = None
    service_cost = None
    if service.service_type == _("Consultation"):
        description = Consultation.objects.get(service_ptr_id=service_id)
        service_cost = description.consultation_type.price
    elif service.service_type == _('Exam'):
        description = Exam.objects.get(service_ptr_id=service_id)
        service_cost = description.exam_type.price
    elif service.service_type == _('Vaccine'):
        description = Vaccine.objects.get(service_ptr_id=service_id)
        service_cost = description.vaccine_type.price

    if request.method == "POST":
        if request.POST['action'] == "save":
            if form.is_valid():
                total = request.POST['total']
                payment = form.save(commit=False)
                payment.total = total
                payment.service_id = service.pk
                payment.save()
                service.paid = 'yes'
                service.save()

                messages.success(request, _('Payment registered successfully.'))
                redirect_url = reverse("unpaid")
                return HttpResponseRedirect(redirect_url)
            else:
                messages.warning(request, _('Information not saved.'))
        else:
            messages.warning(request, _('Action not available.'))

    context = {
        "service": service,
        "description": description,
        "service_cost": service_cost,
        "form": form,
        "creating": True,
    }

    return render(request, template_name, context)
