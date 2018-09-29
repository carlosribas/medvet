# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


from animal.models import *
from animal.forms import AddAnimalForm

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

    def test_create_animal_invalid_form(self):
        data = {
            'owner': 1,
            'specie': 1,
            'breed': 1,
            'animal_name': '',
            'fur': 'long',
            'action': 'save'
        }
        response = self.client.post(reverse("animal_new"), data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Information not saved." in message.message)
