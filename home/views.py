# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import activate, LANGUAGE_SESSION_KEY

from client.models import Client
from animal.models import Animal
from services.models import Service


@login_required
def home(request, template_name="home/home.html"):
    total_of_clients = Client.objects.count()
    total_of_animals = Animal.objects.count()
    last_animals = Animal.objects.all().order_by('-id')[:5]
    last_services = Service.objects.all().order_by('-id')[:5]
    unpaid_service = Service.objects.filter(paid='no')
    total = 0
    for service in unpaid_service:
        total += service.service_cost

    context = {
        'total_of_clients': total_of_clients,
        'total_of_animals': total_of_animals,
        'last_animals': last_animals,
        'last_services': last_services,
        'total': total
    }

    return render(request, template_name, context)


def language_change(request, language_code):
    activate(language_code)
    request.session[LANGUAGE_SESSION_KEY] = language_code
    return HttpResponseRedirect(request.GET['next'])


@login_required
def report(request):
    return render(request, 'reports.html')
