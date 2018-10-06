# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.test import TestCase

from client.views import *
from client.models import Client

from configuration.models import Page

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


def create_client():
    Client.objects.create(name='Fulano de Tal')
    return Client.objects.first()


class ClientTest(TestCase):
    def setUp(self):
        """
        Configure authentication and variables to start each test
        """

        self.user = User.objects.create_user(username=USER_USERNAME, email=USER_EMAIL, password=USER_PWD)
        self.user.is_staff = True
        self.user.save()

        logged = self.client.login(username=USER_USERNAME, password=USER_PWD)
        self.assertEqual(logged, True)

        self.data = {'action': 'save'}

    def fill_contact_form(self):
        self.data['clientcontact_set-TOTAL_FORMS'] = '1'
        self.data['clientcontact_set-INITIAL_FORMS'] = '0'
        self.data['clientcontact_set-MAX_NUM_FORMS'] = ''

    def test_client_new_status_code(self):
        url = reverse('client_new')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/client.html')

    def test_client_new_url_resolves_client_new_view(self):
        view = resolve('/client/new')
        self.assertEquals(view.func, client_new)

    def test_client_new(self):
        url = reverse('client_new')
        self.data = {
            'name': 'John',
            'action': 'save'
        }
        self.fill_contact_form()
        self.client.post(url, self.data)
        self.assertEqual(Client.objects.filter(name='John').count(), 1)

    def test_client_new_wrong_action(self):
        url = reverse('client_new')
        self.data = {
            'name': 'Bill',
            'action': 'bla'
        }
        self.fill_contact_form()
        response = self.client.post(url, self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_client_view_status_code(self):
        client = create_client()
        url = reverse('client_view', args=(client.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/client.html')

    def test_client_view_url_resolves_client_view_view(self):
        view = resolve('/client/view/1/')
        self.assertEquals(view.func, client_view)

    def test_client_view(self):
        client = create_client()
        response = self.client.get(reverse("client_view", args=(client.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Client.objects.count(), 1)

    def test_client_remove(self):
        client = create_client()
        self.data = {
            'action': 'remove'
        }
        response = self.client.post(reverse("client_view", args=(client.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Client.objects.count(), 0)

    def test_client_update_status_code(self):
        client = create_client()
        url = reverse('client_edit', args=(client.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/client.html')

    def test_client_update_url_resolves_client_update_view(self):
        view = resolve('/client/edit/1/')
        self.assertEquals(view.func, client_update)

    def test_client_update(self):
        client = create_client()
        self.data = {
            'name': 'John Bla',
            'email': 'fulano@example.com',
            'action': 'save',
        }
        self.fill_contact_form()
        response = self.client.post(reverse("client_edit", args=(client.id,)), self.data)
        self.assertEqual(response.status_code, 302)

    def test_client_list_status_code(self):
        Page.objects.create(pagination=10)
        url = reverse('client_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/list.html')

    def test_client_list_url_resolves_client_list_view(self):
        view = resolve('/client/list')
        self.assertEquals(view.func, client_list)

    def test_client_list(self):
        create_client()
        list_of_clients = Client.objects.all()
        self.data = {
            'list_of_clients': list_of_clients
        }
        url = reverse('client_list')
        self.client.get(url, self.data)
        self.assertEqual(list_of_clients.count(), 1)

    def test_client_service_list_status_code(self):
        client = create_client()
        url = reverse('client_service_list', args=(client.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/service_list.html')

    def test_client_service_list_url_resolves_client_service_list(self):
        view = resolve('/client/1/services/')
        self.assertEquals(view.func, client_service_list)

    def test_client_service_redirect_to_pay(self):
        client = create_client()
        self.data = {
            'services': [1-2],
            'action': 'pay',
        }
        response = self.client.post(reverse("client_service_list", args=(client.id,)), self.data)
        self.assertEqual(response.status_code, 302)

    def test_client_service_pay_without_service_selected(self):
        client = create_client()
        self.data = {
            'services': [],
            'action': 'pay',
        }
        response = self.client.post(reverse("client_service_list", args=(client.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("You should select at least one service" in message.message)
