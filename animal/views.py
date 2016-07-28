import json as simplejson

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from models import Specie, Animal


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


@login_required
def animal_record(request):
    if request.method == 'POST':
        animal = request.POST['id_animal']
        animal = Animal.objects.get(pk=animal)
        context = {'animal': animal}
        return render(request, 'animal_record.html', context)
