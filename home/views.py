# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import activate, LANGUAGE_SESSION_KEY

from client.models import Client
from animal.models import Animal


@login_required
def home(request, template_name="home/home.html"):
    total_of_clients = Client.objects.count()
    total_of_animals = Animal.objects.count()

    context = {'total_of_clients': total_of_clients, 'total_of_animals': total_of_animals}
    return render(request, template_name, context)


def language_change(request, language_code):
    activate(language_code)
    request.session[LANGUAGE_SESSION_KEY] = language_code
    return HttpResponseRedirect(request.GET['next'])


@login_required
def report(request):
    return render(request, 'reports.html')
