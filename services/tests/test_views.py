# -*- coding: utf-8 -*-
import tempfile

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.core.urlresolvers import resolve
from django.test import TestCase

from services.views import *
from services.models import *

from animal.models import Breed, Specie
from client.models import Client
from configuration.models import Document, Image

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


def create_client_and_animal():
    client = Client.objects.create(name='Fulano de Tal')
    specie = Specie.objects.create(name='Felina')
    breed = Breed.objects.create(specie=specie, name='Maine Coon')
    animal = Animal.objects.create(owner=client, specie=specie, breed=breed, animal_name='Bidu', fur='l')
    return animal


def create_consultation():
    animal = create_client_and_animal()
    consultation_type = ConsultationType.objects.create(name='Consulta', price='0')
    consultation = Consultation.objects.create(
        animal=animal,
        date=datetime.date.today(),
        consultation_type=consultation_type
    )
    return consultation


def create_vaccine():
    animal = create_client_and_animal()
    vaccine_type = VaccineType.objects.create(name='Raiva', price='0')
    vaccine = Vaccine.objects.create(animal=animal, date=datetime.date.today(), vaccine_type=vaccine_type)
    return vaccine


def create_exam():
    animal = create_client_and_animal()
    exam_category = ExamCategory.objects.create(name='Endocrinologia')
    exam_name = ExamName.objects.create(name='Insulina', price='0', category=exam_category)
    exam = Exam.objects.create(animal=animal, date=datetime.date.today())
    exam.exam_list.add(exam_name)
    return exam


def create_image():
    image = tempfile.NamedTemporaryFile(suffix=".jpg").name
    logo = Image.objects.create(logo=image)
    return logo


def create_document():
    return Document.objects.create(footer='Test Config')


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

    def test_consultation_new_status_code(self):
        animal = create_client_and_animal()
        url = reverse('consultation_new', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_consultation_new_url_resolves_consultation_new_view(self):
        view = resolve('/service/consultation/new/1/')
        self.assertEquals(view.func, consultation_new)

    def test_create_consultation(self):
        animal = create_client_and_animal()
        consultation_type = ConsultationType.objects.create(name='Retorno', price='0')
        title = 'Testando consulta'
        self.data = {
            'animal': animal.id,
            'consultation_type': consultation_type.id,
            'date': datetime.date.today(),
            'title': title,
            'action': 'save'
        }
        response = self.client.post(reverse("consultation_new", args=(animal.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        consultation = Consultation.objects.filter(title=title)
        self.assertEqual(consultation.count(), 1)
        self.assertTrue(isinstance(consultation[0], Consultation))
        self.assertTrue(isinstance(consultation_type, ConsultationType))
        self.assertEqual(consultation_type.__str__(), consultation_type.name)

    def test_create_consultation_wrong_action(self):
        animal = create_client_and_animal()
        consultation_type = ConsultationType.objects.create(name='Retorno', price='0')
        title = 'Testando consulta'
        self.data = {
            'animal': animal.id,
            'consultation_type': consultation_type.id,
            'date': datetime.date.today(),
            'title': title,
            'action': 'bla'
        }
        response = self.client.post(reverse("consultation_new", args=(animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_consultation_list_status_code(self):
        animal = create_client_and_animal()
        url = reverse('consultation_list', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_consultation_list_url_resolves_consultation_list_view(self):
        view = resolve('/service/consultation/list/1/')
        self.assertEquals(view.func, consultation_list)

    def test_consultation_list_remove_consultation(self):
        animal = create_client_and_animal()
        create_consultation()
        self.assertEqual(Consultation.objects.count(), 1)
        self.data = {
            'consultation_type': 1,
            'date': datetime.date.today(),
            'action': 'remove_consultation-1'
        }
        self.client.post(reverse("consultation_list", args=(animal.id,)), self.data)
        self.assertEqual(Consultation.objects.count(), 0)

    def test_consultation_list_remove_consultation_wrong_action(self):
        animal = create_client_and_animal()
        create_consultation()
        self.data = {
            'consultation_type': 1,
            'date': datetime.date.today(),
            'action': 'bla'
        }
        response = self.client.post(reverse("consultation_list", args=(animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_consultation_view_status_code(self):
        consultation = create_consultation()
        url = reverse('consultation_view', args=(consultation.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/consultation_view_or_update.html')

    def test_consultation_view_url_resolves_consultation_view_view(self):
        view = resolve('/service/consultation/view/1/')
        self.assertEquals(view.func, consultation_view)

    def test_consultation_view_remove_vaccine(self):
        animal = create_client_and_animal()
        consultation = create_consultation()
        vaccine = create_vaccine()
        vaccine.vaccine_in_consultation = consultation
        vaccine.save()
        self.data = {
            'vaccine_type': 1,
            'date': datetime.date.today(),
            'action': 'remove_vaccine-2'
        }
        self.client.post(reverse("consultation_view", args=(animal.id,)), self.data)
        self.assertEqual(Vaccine.objects.count(), 0)

    def test_consultation_view_remove_exam(self):
        animal = create_client_and_animal()
        consultation = create_consultation()
        exam = create_exam()
        exam.vaccine_in_consultation = consultation
        exam.save()
        self.data = {
            'action': 'remove_exam-2'
        }
        self.client.post(reverse("consultation_view", args=(animal.id,)), self.data)
        self.assertEqual(Vaccine.objects.count(), 0)

    def test_consultation_view_wrong_action(self):
        animal = create_client_and_animal()
        create_consultation()
        self.data = {
            'action': 'bla'
        }
        response = self.client.post(reverse("consultation_view", args=(animal.id,)), self.data)
        message = list(get_messages(response.wsgi_request))
        self.assertEqual(len(message), 1)
        self.assertEqual(str(message[0]), 'Action not available.')

    def test_consultation_update_status_code(self):
        consultation = create_consultation()
        url = reverse('consultation_update', args=(consultation.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/consultation_view_or_update.html')

    def test_consultation_update_url_resolves_consultation_update_view(self):
        view = resolve('/service/consultation/edit/1/')
        self.assertEquals(view.func, consultation_update)

    def test_update_consultation(self):
        animal = create_client_and_animal()
        consultation = create_consultation()
        self.data = {
            'animal': animal.id,
            'consultation_type': consultation.id,
            'date': datetime.date.today(),
            'title': 'titulo atualizado',
            'action': 'save'
        }
        response = self.client.post(reverse("consultation_update", args=(consultation.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        consultation_updated = Consultation.objects.filter(title='titulo atualizado')
        self.assertEqual(consultation_updated.count(), 1)

    def test_update_consultation_wrong_action(self):
        create_client_and_animal()
        consultation = create_consultation()
        self.data = {
            'action': 'bla'
        }
        response = self.client.post(reverse("consultation_update", args=(consultation.id,)), self.data)
        message = list(get_messages(response.wsgi_request))
        self.assertEqual(len(message), 1)
        self.assertEqual(str(message[0]), 'Action not available.')

    def test_vaccine_in_consultation_status_code(self):
        animal = create_client_and_animal()
        consultation = create_consultation()
        url = reverse('vaccine_in_consultation', args=(consultation.id, animal.id))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_vaccine_in_consultation_url_resolves_vaccine_in_consultation_view(self):
        view = resolve('/service/consultation/1/animal/1/vaccine/new/')
        self.assertEquals(view.func, vaccine_new)

    def test_exam_in_consultation_status_code(self):
        animal = create_client_and_animal()
        consultation = create_consultation()
        url = reverse('exam_in_consultation', args=(consultation.id, animal.id))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_exam_in_consultation_url_resolves_exam_in_consultation_view(self):
        view = resolve('/service/consultation/1/animal/1/exam/new/')
        self.assertEquals(view.func, exam_new)

    def test_vaccine_new_status_code(self):
        animal = create_client_and_animal()
        url = reverse('vaccine_new', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_vaccine_new_url_resolves_vaccine_new_view(self):
        view = resolve('/service/vaccine/new/1/')
        self.assertEquals(view.func, vaccine_new)

    def test_vaccine_new(self):
        animal = create_client_and_animal()
        vaccine_type = VaccineType.objects.create(name='Gripe', price='0')
        self.data = {
            'animal': animal.id,
            'vaccine_type': vaccine_type.id,
            'date': datetime.date.today(),
            'action': 'save'
        }
        response = self.client.post(reverse("vaccine_new", args=(animal.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        vaccine = Vaccine.objects.filter(date=datetime.date.today())
        self.assertEqual(vaccine.count(), 1)
        self.assertTrue(isinstance(vaccine[0], Vaccine))
        self.assertTrue(isinstance(vaccine_type, VaccineType))
        self.assertEqual(vaccine_type.__str__(), vaccine_type.name)

    def test_vaccine_new_wrong_action(self):
        animal = create_client_and_animal()
        vaccine_type = VaccineType.objects.create(name='Gripe', price='0')
        self.data = {
            'animal': animal.id,
            'vaccine_type': vaccine_type.id,
            'date': datetime.date.today(),
            'action': 'bla'
        }
        response = self.client.post(reverse("vaccine_new", args=(animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_vaccine_list_status_code(self):
        animal = create_client_and_animal()
        url = reverse('vaccine_list', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_vaccine_list_remove_vaccine(self):
        vaccine = create_vaccine()
        self.data = {
            'action': 'remove_vaccine-1'
        }
        self.client.post(reverse("vaccine_list", args=(vaccine.animal.id,)), self.data)
        vaccine = Exam.objects.filter(date=datetime.date.today())
        self.assertEqual(vaccine.count(), 0)

    def test_vaccine_list_remove_wrong_action(self):
        vaccine = create_vaccine()
        self.data = {
            'action': 'bla'
        }
        response = self.client.post(reverse("vaccine_list", args=(vaccine.animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_vaccine_view_status_code(self):
        vaccine = create_vaccine()
        url = reverse('vaccine_view', args=(vaccine.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/vaccine_view_or_update.html')

    def test_vaccine_view_url_resolves_vaccine_view_view(self):
        view = resolve('/service/vaccine/view/1/')
        self.assertEquals(view.func, vaccine_view)

    def test_vaccine_list_url_resolves_vaccine_list_view(self):
        view = resolve('/service/vaccine/list/1/')
        self.assertEquals(view.func, vaccine_list)

    def test_vaccine_update_status_code(self):
        vaccine = create_vaccine()
        url = reverse('vaccine_update', args=(vaccine.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/vaccine_view_or_update.html')

    def test_vaccine_update_url_resolves_vaccine_update_view(self):
        view = resolve('/service/vaccine/edit/1/')
        self.assertEquals(view.func, vaccine_update)

    def test_vaccine_update(self):
        vaccine = create_vaccine()
        self.data = {
            'animal': 1,
            'vaccine_type': 1,
            'date': datetime.date.today(),
            'note': 'vaccine updated',
            'action': 'save'
        }
        response = self.client.post(reverse("vaccine_update", args=(vaccine.animal.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        vaccine_updated = Vaccine.objects.filter(note='vaccine updated')
        self.assertEqual(vaccine_updated.count(), 1)

    def test_vaccine_update_wrong_action(self):
        vaccine = create_vaccine()
        self.data = {
            'animal': 1,
            'vaccine_type': 1,
            'date': datetime.date.today(),
            'note': 'vaccine updated',
            'action': 'bla'
        }
        response = self.client.post(reverse("vaccine_update", args=(vaccine.animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_vaccine_booster_list_status_code(self):
        url = reverse('vaccine_booster_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/vaccine_booster_list.html')

    def test_vaccine_booster_list_url_resolves_vaccine_booster_list_view(self):
        view = resolve('/service/vaccine/booster_list')
        self.assertEquals(view.func, vaccine_booster_list)

    def test_exam_new_status_code(self):
        animal = create_client_and_animal()
        url = reverse('exam_new', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_exam_new_url_resolves_exam_new_view(self):
        view = resolve('/service/exam/new/1/')
        self.assertEquals(view.func, exam_new)

    def test_create_exam(self):
        animal = create_client_and_animal()
        exam_category = ExamCategory.objects.create(name='Microbiologia')
        exam_name = ExamName.objects.create(name='Cultura para fungo', price='0', category=exam_category)
        self.data = {
            'animal': animal.id,
            'to': [exam_name.id],
            'exam_type': 'request',
            'date': datetime.date.today().strftime('%d/%m/%Y'),
            'action': 'save'
        }
        response = self.client.post(reverse("exam_new", args=(animal.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        exam = Exam.objects.filter(date=datetime.date.today())
        self.assertEqual(exam.count(), 1)
        self.assertTrue(isinstance(exam_category, ExamCategory))
        self.assertTrue(isinstance(exam_name, ExamName))
        self.assertEqual(exam_category.__str__(), exam_category.name)
        self.assertEqual(exam_name.__str__(), exam_name.name)

    def test_create_exam_wrong_action(self):
        animal = create_client_and_animal()
        exam_category = ExamCategory.objects.create(name='Microbiologia')
        exam_name = ExamName.objects.create(name='Cultura para fungo', price='0', category=exam_category)
        self.data = {
            'animal': animal.id,
            'to': [exam_name.id],
            'exam_type': 'request',
            'date': datetime.date.today().strftime('%d/%m/%Y'),
            'action': 'bla'
        }
        response = self.client.post(reverse("exam_new", args=(animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_create_exam_without_select_exam(self):
        animal = create_client_and_animal()
        exam_category = ExamCategory.objects.create(name='Microbiologia')
        ExamName.objects.create(name='Cultura para fungo', price='0', category=exam_category)
        self.data = {
            'animal': animal.id,
            'to': [],
            'exam_type': 'request',
            'date': datetime.date.today().strftime('%d/%m/%Y'),
            'action': 'save'
        }
        response = self.client.post(reverse("exam_new", args=(animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("You have to select at least one exam." in message.message)

    def test_exam_view_status_code(self):
        exam = create_exam()
        url = reverse('exam_view', args=(exam.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/exam_view_or_update.html')

    def test_exam_view_url_resolves_exam_view_view(self):
        view = resolve('/service/exam/view/1/')
        self.assertEquals(view.func, exam_view)

    def test_exam_list_status_code(self):
        animal = create_client_and_animal()
        url = reverse('exam_list', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_exam_list_url_resolves_exam_list_view(self):
        view = resolve('/service/exam/list/1/')
        self.assertEquals(view.func, exam_list)

    def test_exam_list_remove_exam(self):
        exam = create_exam()
        self.data = {
            'action': 'remove_exam-1'
        }
        self.client.post(reverse("exam_list", args=(exam.animal.id,)), self.data)
        exam = Exam.objects.filter(date=datetime.date.today())
        self.assertEqual(exam.count(), 0)

    def test_exam_list_wrong_action(self):
        exam = create_exam()
        self.data = {
            'action': 'bla'
        }
        response = self.client.post(reverse("exam_list", args=(exam.animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_exam_list_create_pdf(self):
        create_image()
        create_document()
        exam = create_exam()
        self.data = {
            'action': 'create_pdf-1'
        }
        self.client.post(reverse("exam_list", args=(exam.animal.id,)), self.data)

    def test_exam_update_status_code(self):
        exam = create_exam()
        url = reverse('exam_update', args=(exam.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/exam_view_or_update.html')

    def test_exam_update_url_resolves_exam_update_view(self):
        view = resolve('/service/exam/edit/1/')
        self.assertEquals(view.func, exam_update)

    def test_exam_update(self):
        exam = create_exam()
        self.data = {
            'animal': 1,
            'to': [1],
            'exam_type': 'request',
            'date': datetime.date.today().strftime('%d/%m/%Y'),
            'note': 'exam updated',
            'action': 'save'
        }
        response = self.client.post(reverse("exam_update", args=(exam.animal.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        exam_updated = Exam.objects.filter(note='exam updated')
        self.assertEqual(exam_updated.count(), 1)

    def test_exam_update_wrong_action(self):
        exam = create_exam()
        self.data = {
            'animal': 1,
            'to': [1],
            'exam_type': 'request',
            'date': datetime.date.today().strftime('%d/%m/%Y'),
            'note': 'exam updated',
            'action': 'bla'
        }
        response = self.client.post(reverse("exam_update", args=(exam.animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Action not available." in message.message)

    def test_exam_update_without_exam(self):
        exam = create_exam()
        self.data = {
            'animal': 1,
            'to': [],
            'exam_type': 'request',
            'date': datetime.date.today().strftime('%d/%m/%Y'),
            'note': 'exam updated',
            'action': 'save'
        }
        response = self.client.post(reverse("exam_update", args=(exam.animal.id,)), self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("You have to select at least one exam." in message.message)

    def test_exam_path(self):
        animal = create_client_and_animal()
        exam = create_exam()
        filename = 'exam.pdf'
        path = 'exams/{0}/{1}/{2}'.format(animal.animal_name, datetime.date.today().strftime('%d-%m-%Y'), filename)
        created_path = exam_path(exam, filename)
        self.assertEqual(path, created_path)
