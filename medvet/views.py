from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import activate, LANGUAGE_SESSION_KEY

from client.models import Client
from animal.models import Animal


@login_required
def index(request):
    clients = Client.objects.all()
    animals = Animal.objects.all()
    context = {'clients': clients, 'animals': animals}
    return render(request, 'index.html', context)


def language_change(request, language_code):
    activate(language_code)
    request.session[LANGUAGE_SESSION_KEY] = language_code

    return HttpResponseRedirect(request.GET['next'])
