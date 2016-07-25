from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from client.models import Client
from animal.models import Animal


@login_required
def index(request):
    clients = Client.objects.count()
    animals = Animal.objects.count()
    context = {'clients': clients, 'animals': animals}
    return render(request, 'index.html', context)