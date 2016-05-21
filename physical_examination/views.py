import json as simplejson
from animal.models import Animal
from client.models import Client
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.


def select_animal(request):
    if request.method == 'GET':
        owner_id = request.GET.get('owner')
        owner = get_object_or_404(Client, id=owner_id)

        select = Animal.objects.filter(owner=owner)
        animal = []
        for a in select:
            animal.append({'pk': a.id, 'valor': a.__unicode__()})

        json = simplejson.dumps(animal)
        return HttpResponse(json, content_type="application/json")
