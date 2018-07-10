# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from services.models import Service


@login_required
def unpaid(request, template_name="payment/unpaid.html"):
    unpaid_list = Service.objects.filter(paid='no').order_by('date')
    context = {"unpaid_list": unpaid_list}
    return render(request, template_name, context)