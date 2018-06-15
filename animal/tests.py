# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.test import TestCase

from views import *
from models import *
from forms import AddAnimalForm

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


class AnimalTest(TestCase):
    def setUp(self):
        """
        Configure authentication and variables to start each test
        """

        self.user = User.objects.create_user(username=USER_USERNAME, email=USER_EMAIL, password=USER_PWD)
        self.user.is_staff = True
        self.user.save()

        logged = self.client.login(username=USER_USERNAME, password=USER_PWD)
        self.assertEqual(logged, True)

        client = Client.objects.create(name='Fulano de Tal')
        specie = Specie.objects.create(name='Felina')
        breed = Breed.objects.create(specie=specie, name='Maine Coon')
        Animal.objects.create(owner=client, specie=specie, breed=breed, animal_name='Bidu', fur='l')

    def test_animal_new_status_code(self):
        url = reverse('animal_new')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_new.html')

    def test_animal_new_url_resolves_animal_new_view(self):
        view = resolve('/animal/new')
        self.assertEquals(view.func, animal_new)

    def test_animal_view_status_code(self):
        animal = Animal.objects.first()
        url = reverse('animal_view', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_animal_view_url_resolves_anima_view_view(self):
        view = resolve('/animal/view/1/')
        self.assertEquals(view.func, animal_view)

    def test_animal_update_status_code(self):
        animal = Animal.objects.first()
        url = reverse('animal_edit', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_animal_update_url_resolves_animal_update_view(self):
        view = resolve('/animal/edit/1/')
        self.assertEquals(view.func, animal_update)

    def test_create_animal(self):
        client = Client.objects.create(name='John')
        specie = Specie.objects.create(name='Canina')
        breed = Breed.objects.create(specie=specie, name='Golden')
        animal = Animal.objects.create(owner=client, specie=specie, breed=breed, animal_name='Teddy', fur='l')
        self.assertTrue(isinstance(animal, Animal))
        self.assertEqual(animal.__unicode__(), animal.animal_name)

    #
    # Testing forms
    #

    def test_valid_animal_form(self):
        data = {'owner': 1, 'specie': 1, 'breed': 1, 'animal_name': 'Chico'}
        form = AddAnimalForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_animal_form(self):
        """
        Using empty value to the animal_name field
        """
        data = {'owner': 1, 'specie': 1, 'breed': 1, 'animal_name': ''}
        form = AddAnimalForm(data=data)
        self.assertFalse(form.is_valid())
