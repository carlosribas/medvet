# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from payment.views import unpaid, payment_new, payment_view, payment_edit
from payment.models import PaymentRegister
from client.models import Client
from animal.models import Animal, Breed, Specie
from services.models import ConsultationType, Consultation, Exam, ExamCategory, ExamName, VaccineType, Vaccine

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


def create_client_and_animal():
    client = Client.objects.create(name='Fulano de Tal')
    specie = Specie.objects.create(name='Felina')
    breed = Breed.objects.create(specie=specie, name='Maine Coon')
    animal = Animal.objects.create(owner=client, specie=specie, breed=breed, animal_name='Bidu', fur='l')
    return animal


def payment_consultation():
    payment = PaymentRegister.objects.create(
        installment='1x',
        discount_or_increase='0',
        total='250.00',
        installment_value='250.00'
    )

    animal = create_client_and_animal()
    consultation_type = ConsultationType.objects.create(name='Consulta', price="200.00")
    consultation = Consultation.objects.create(
        animal=animal,
        date=datetime.date.today(),
        consultation_type=consultation_type,
        payment = payment,
    )
    return consultation


def payment_vaccine():
    animal = create_client_and_animal()
    vaccine_type = VaccineType.objects.create(name='Vacina', price="100.00")
    vaccine = Vaccine.objects.create(
        animal=animal,
        date=datetime.date.today(),
        vaccine_type=vaccine_type
    )
    return vaccine


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

    def fill_payment_form(self):
        self.data['payment_set-TOTAL_FORMS'] = '1'
        self.data['payment_set-INITIAL_FORMS'] = '0'
        self.data['payment_set-MAX_NUM_FORMS'] = ''

    def test_unpaid_view_status_code(self):
        url = reverse('unpaid')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_unpaid_url_resolves_unpaid_view(self):
        view = resolve('/payment/unpaid')
        self.assertEquals(view.func, unpaid)

    def test_payment_new_view_status_code(self):
        consultation = payment_consultation()
        url = reverse('payment_new', args=(consultation.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_payment_new_url_resolves_payment_new_view(self):
        view = resolve('/payment/services/1')
        self.assertEquals(view.func, payment_new)

    def test_payment_new(self):
        payment_vaccine()
        self.assertEqual(PaymentRegister.objects.count(), 0)
        self.data = {
            'installment': '1x',
            'discount_or_increase': '-10.00',
            'total': '350.00',
            'installment_value': '0',
            'action': 'save'
        }
        self.fill_payment_form()
        service_list = '1'
        response = self.client.post(reverse("payment_new", args=(service_list,)), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PaymentRegister.objects.count(), 1)

    def test_payment_new_with_wrong_action(self):
        consultation = payment_consultation()
        self.data = {
            'service': consultation.pk,
            'action': 'bla'
        }
        response = self.client.post(reverse("payment_new", args=(consultation.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Information not saved." in message.message)

    def test_payment_view_status_code(self):
        payment = payment_consultation()
        url = reverse('payment_view', args=(payment.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_payment_view_url_resolves_payment_view_view(self):
        view = resolve('/payment/view/1/')
        self.assertEquals(view.func, payment_view)

    def test_payment_edit_status_code(self):
        payment = payment_consultation()
        url = reverse('payment_edit', args=(payment.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_payment_edit_url_resolves_payment_edit_view(self):
        view = resolve('/payment/edit/1/')
        self.assertEquals(view.func, payment_edit)
