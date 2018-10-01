# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from services.models import *
from services.forms import ConsultationForm, ExamForm, VaccineForm
from animal.models import Breed, Specie
from client.models import Client

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


class ServiceTest(TestCase):
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
        vaccine_type = VaccineType.objects.create(name='Raiva', price='0')
        Vaccine.objects.create(animal=animal, date=datetime.date.today(), vaccine_type=vaccine_type)
        exam_category = ExamCategory.objects.create(name='Endocrinologia')
        exam_name = ExamName.objects.create(name='Insulina', price='0', category=exam_category)
        exam = Exam.objects.create(animal=animal, date=datetime.date.today())
        exam.exam_list.add(exam_name)

    def test_valid_consultation_form(self):
        data = {'consultation_type': 1, 'date': datetime.date.today(), 'title': 'Lorem ipsum'}
        form = ConsultationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_consultation_form(self):
        """
        Using empty date
        """
        data = {'consultation_type': 1, 'date': '', 'title': 'Lorem ipsum'}
        form = ConsultationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_create_consultation_invalid_form(self):
        data = {
            'animal': 1,
            'consultation_type': 1,
            'date': '',
            'action': 'save'
        }
        response = self.client.post(reverse("consultation_new", args=(1,)), data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Information not saved." in message.message)

    def test_update_consultation_invalid_form(self):
        data = {
            'animal': 1,
            'consultation_type': 1,
            'date': '',
            'action': 'save'
        }
        response = self.client.post(reverse("consultation_update", args=(1,)), data)
        message = list(get_messages(response.wsgi_request))
        self.assertEqual(len(message), 1)
        self.assertEqual(str(message[0]), 'Information not saved.')

    def test_valid_vaccine_form(self):
        data = {'vaccine_type': 1, 'date': datetime.date.today()}
        form = VaccineForm(initial={'specie': 1}, data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_vaccine_form(self):
        """
        Using empty date
        """
        data = {'vaccine_type': 1, 'date': ''}
        form = VaccineForm(initial={'specie': 1}, data=data)
        self.assertFalse(form.is_valid())

    def test_vaccine_new_invalid_form(self):
        data = {
            'animal': 1,
            'vaccine_type': 1,
            'date': '',
            'action': 'save'
        }
        response = self.client.post(reverse("vaccine_new", args=(1,)), data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Information not saved." in message.message)

    def test_valid_exam_form(self):
        exam_category = ExamCategory.objects.create(name='Microbiologia')
        exam = ExamName.objects.create(name='Cultura para fungo', price='0', category=exam_category)
        data = {'date': datetime.date.today(), 'exam_list': exam, 'exam_type': 'request'}
        form = ExamForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_exam_form(self):
        """
        Using empty date
        """
        data = {'date': ''}
        form = ExamForm(data=data)
        self.assertFalse(form.is_valid())
