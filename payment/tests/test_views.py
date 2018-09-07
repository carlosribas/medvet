# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from payment.views import unpaid, client_payment
from client.models import Client
from animal.models import Animal, Breed, Specie
from services.models import ConsultationType, Consultation

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


class PaymentTest(TestCase):
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
        animal = Animal.objects.create(owner=client, specie=specie, breed=breed, animal_name='Bidu', fur='l')
        consultation_type = ConsultationType.objects.create(name='Consulta', price='0')
        Consultation.objects.create(animal=animal, date=datetime.date.today(), consultation_type=consultation_type)

    def test_unpaid_view_status_code(self):
        url = reverse('unpaid')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_unpaid_url_resolves_unpaid_view(self):
        view = resolve('/payment/unpaid')
        self.assertEquals(view.func, unpaid)

    def test_client_payment_view_status_code(self):
        consultation = Consultation.objects.first()
        url = reverse('client_payment', args=(consultation.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_client_payment_url_resolves_client_payment_view(self):
        view = resolve('/payment/services/1')
        self.assertEquals(view.func, client_payment)
