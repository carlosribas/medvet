from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from client.models import Client
from animal.models import Animal


@login_required
def index(request):
    clients = Client.objects.all()
    animals = Animal.objects.all()
    context = {'clients': clients, 'animals': animals}
    return render(request, 'index.html', context)


@login_required
def animal_record(request):
    if request.method == 'POST':
        animal = request.POST['id_animal']
        animal = Animal.objects.get(pk=animal)
        context = {'animal': animal}
        return render(request, 'animal_record.html', context)