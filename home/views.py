# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import activate, LANGUAGE_SESSION_KEY, ugettext as _

from client.models import Client
from animal.models import Animal


def authentication(request):
    return render(request, 'authentication.html')


@login_required
def home(request):
    clients = Client.objects.all()
    animals = Animal.objects.all()

    if request.method == 'POST':
        animal_id = request.POST['animal']
        if animal_id != '0' and animal_id != '':
            redirect_url = reverse('animal_view', args=(animal_id,))
            return HttpResponseRedirect(redirect_url)
        else:
            messages.warning(request, _("You should select an animal."))

    context = {'clients': clients, 'animals': animals}
    return render(request, 'home/home.html', context)


def language_change(request, language_code):
    activate(language_code)
    request.session[LANGUAGE_SESSION_KEY] = language_code
    return HttpResponseRedirect(request.GET['next'])