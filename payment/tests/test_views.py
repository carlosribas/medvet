# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from payment.views import unpaid, client_payment
from payment.models import Payment, PaymentMethod
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
    animal = create_client_and_animal()
    consultation_type = ConsultationType.objects.create(name='Consulta', price="200.00")
    consultation = Consultation.objects.create(
        animal=animal,
        date=datetime.date.today(),
        consultation_type=consultation_type
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


def payment_exam():
    animal = create_client_and_animal()
    exam_category = ExamCategory.objects.create(name='Endocrinologia')
    exam_name = ExamName.objects.create(name='Insulina', price='50.00', category=exam_category)
    exam = Exam.objects.create(animal=animal, date=datetime.date.today())
    exam.exam_list.add(exam_name)
    return exam


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

    def test_unpaid_view_status_code(self):
        url = reverse('unpaid')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_unpaid_url_resolves_unpaid_view(self):
        view = resolve('/payment/unpaid')
        self.assertEquals(view.func, unpaid)

    def test_client_payment_view_status_code(self):
        consultation = payment_consultation()
        url = reverse('client_payment', args=(consultation.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_client_payment_url_resolves_client_payment_view(self):
        view = resolve('/payment/services/1')
        self.assertEquals(view.func, client_payment)

    def test_payment_service(self):
        consultation = payment_consultation()
        vaccine = payment_vaccine()
        exam = payment_exam()
        payment_method = PaymentMethod.objects.create(name="Dinheiro")
        self.assertEqual(Payment.objects.count(), 0)
        self.data = {
            'service': [consultation.pk, vaccine.pk, exam.pk],
            'payment_method': payment_method.pk,
            'date': datetime.date.today().strftime('%d/%m/%Y'),
            'total': '350.00',
            'action': 'save'
        }
        service_list = '1-2-3'
        response = self.client.post(reverse("client_payment", args=(service_list,)), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Payment.objects.count(), 3)

    def test_payment_service_wrong_action(self):
        consultation = payment_consultation()
        payment_method = PaymentMethod.objects.create(name="Dinheiro")
        self.data = {
            'service': consultation.pk,
            'payment_method': payment_method.pk,
            'date': datetime.date.today().strftime('%d/%m/%Y'),
            'total': '200.00',
            'action': 'bla'
        }
        response = self.client.post(reverse("client_payment", args=(consultation.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Information not saved." in message.message)
