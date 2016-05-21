import json as simplejson
from animal.models import Specie
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.


def select_specie(request):
    if request.method == 'GET':
        specie_id = request.GET.get('specie')
        specie = get_object_or_404(Specie, id=specie_id)

        breeds = specie.breed_set.all()
        list_breed = []
        for a in breeds:
            list_breed.append({'pk': a.id, 'valor': a.__unicode__()})

        colors = specie.color_set.all()
        list_color = []
        for a in colors:
            list_color.append({'pk': a.id, 'valor': a.__unicode__()})

        json = simplejson.dumps([list_breed, list_color])
        return HttpResponse(json, content_type="application/json")
