# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from services.models import Service


@login_required
def unpaid(request, template_name="payment/unpaid.html"):
    unpaid_list = Service.objects.filter(paid='no').order_by('date')

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
                unpaid_list = Service.objects.filter(
                    paid='no',
                    date__gte=start_date,
                    date__lte=end_date
                ).order_by('date')

    context = {"unpaid_list": unpaid_list}
    return render(request, template_name, context)
