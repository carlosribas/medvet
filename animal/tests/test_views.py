# -*- coding: utf-8 -*-
from datetime import timedelta
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.test import TestCase

from animal.views import *
from animal.models import *

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
        color = Color.objects.create(specie=specie, name='Black')
        Animal.objects.create(owner=client, specie=specie, breed=breed, color=color, animal_name='Bidu', fur='l')

    def test_animal_new_status_code(self):
        url = reverse('animal_new')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_new.html')

    def test_animal_new_url_resolves_animal_new_view(self):
        view = resolve('/animal/new')
        self.assertEquals(view.func, animal_new)

    def test_animal_new(self):
        url = reverse('animal_new')
        self.data = {
            'owner': 1,
            'specie': 1,
            'breed': 1,
            'animal_name': 'Chico',
            'fur': 'long',
            'action': 'save'
        }
        self.client.post(url, self.data)
        animal = Animal.objects.filter(animal_name='Chico')
        self.assertEqual(animal.count(), 1)
        self.assertTrue(isinstance(animal[0], Animal))
        self.assertEqual(animal[0].__str__(), animal[0].animal_name)
        self.assertEqual(animal[0].age(), None)

    def test_animal_new_wrong_action(self):
        url = reverse('animal_new')
        self.data = {
            'owner': 1,
            'specie': 1,
            'breed': 1,
            'animal_name': 'Chico',
            'fur': 'long',
            'action': 'bla'
        }
        response = self.client.post(url, self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_animal_view_status_code(self):
        animal = Animal.objects.first()
        url = reverse('animal_view', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_animal_view_url_resolves_anima_view_view(self):
        view = resolve('/animal/view/1/')
        self.assertEquals(view.func, animal_view)

    def test_animal_view(self):
        animal = Animal.objects.first()
        response = self.client.get(reverse("animal_view", args=(animal.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Animal.objects.count(), 1)

    def test_animal_remove(self):
        animal = Animal.objects.first()
        self.data = {
            'action': 'remove'
        }
        response = self.client.post(reverse("animal_view", args=(animal.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Animal.objects.count(), 0)

    def test_animal_update_status_code(self):
        animal = Animal.objects.first()
        url = reverse('animal_edit', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_animal_update_url_resolves_animal_update_view(self):
        view = resolve('/animal/edit/1/')
        self.assertEquals(view.func, animal_update)

    def test_animal_update(self):
        animal = Animal.objects.first()
        self.data = {
            'owner': 1,
            'specie': 1,
            'breed': 1,
            'animal_name': 'Chico',
            'fur': 'long',
            'birthdate': datetime.date.today() - timedelta(days=740),
            'action': 'save'
        }
        response = self.client.post(reverse("animal_edit", args=(animal.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        animal = Animal.objects.filter(animal_name='Chico')
        self.assertEqual(animal.count(), 1)
        self.assertEqual(animal[0].age(), 2)

    def test_animal_search_status_code(self):
        Page.objects.create(pagination=10)
        url = reverse('animal_search')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_search.html')

    def test_animal_search_url_resolves_animal_search_view(self):
        view = resolve('/animal/search')
        self.assertEquals(view.func, animal_search)

    def test_animal_search(self):
        animal_list = Animal.objects.all()
        self.data = {
            'animal_list': animal_list
        }
        url = reverse('animal_search')
        self.client.get(url, self.data)
        self.assertEqual(animal_list.count(), 1)

    def test_select_specie_url_resolves_select_specie_view(self):
        view = resolve('/animal/select_specie')
        self.assertEquals(view.func, select_specie_to_filter_breed_and_color)

    def test_select_specie(self):
        Animal.objects.first()
        self.data = {
            'specie': 1,
        }
        response = self.client.get(reverse("select_specie"), self.data)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [[{'pk': 1, 'animal_name': 'Maine Coon'}], [{'pk': 1, 'animal_name': 'Black'}]]
        )
