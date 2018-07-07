# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.test import TestCase

from views import *
from models import *
from forms import ConsultationForm, ExamForm, VaccineForm

from animal.models import Breed, Specie

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
        exam_type = ExamType.objects.create(name='Insulina', price='0', category=exam_category)
        exam = Exam.objects.create(animal=animal, date=datetime.date.today())
        exam.exam_type.add(exam_type)

    def test_consultation_new_status_code(self):
        animal = Animal.objects.first()
        url = reverse('consultation_new', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_consultation_new_url_resolves_consultation_new_view(self):
        view = resolve('/service/consultation/new/1/')
        self.assertEquals(view.func, consultation_new)

    def test_consultation_list_status_code(self):
        animal = Animal.objects.first()
        url = reverse('consultation_list', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_consultation_list_url_resolves_consultation_list_view(self):
        view = resolve('/service/consultation/list/1/')
        self.assertEquals(view.func, consultation_list)

    def test_consultation_view_status_code(self):
        consultation = Consultation.objects.first()
        url = reverse('consultation_view', args=(consultation.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/consultation_view_or_update.html')

    def test_consultation_view_url_resolves_consultation_view_view(self):
        view = resolve('/service/consultation/view/1/')
        self.assertEquals(view.func, consultation_view)

    def test_consultation_update_status_code(self):
        consultation = Consultation.objects.first()
        url = reverse('consultation_update', args=(consultation.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/consultation_view_or_update.html')

    def test_consultation_update_url_resolves_consultation_update_view(self):
        view = resolve('/service/consultation/edit/1/')
        self.assertEquals(view.func, consultation_update)

    def test_vaccine_in_consultation_status_code(self):
        animal = Animal.objects.first()
        consultation = Consultation.objects.first()
        url = reverse('vaccine_in_consultation', args=(consultation.id, animal.id))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_vaccine_in_consultation_url_resolves_vaccine_in_consultation_view(self):
        view = resolve('/service/consultation/1/animal/1/vaccine/new/')
        self.assertEquals(view.func, vaccine_new)

    def test_exam_in_consultation_status_code(self):
        animal = Animal.objects.first()
        consultation = Consultation.objects.first()
        url = reverse('exam_in_consultation', args=(consultation.id, animal.id))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_exam_in_consultation_url_resolves_exam_in_consultation_view(self):
        view = resolve('/service/consultation/1/animal/1/exam/new/')
        self.assertEquals(view.func, exam_new)

    def test_create_consultation(self):
        animal = Animal.objects.first()
        consultation_type = ConsultationType.objects.create(name='Retorno', price='0')
        consultation = Consultation.objects.create(animal=animal, date=datetime.date.today(), consultation_type=consultation_type)
        self.assertTrue(isinstance(consultation_type, ConsultationType))
        self.assertTrue(isinstance(consultation, Consultation))
        self.assertEqual(consultation_type.__str__(), consultation_type.name)

    def test_vaccine_new_status_code(self):
        animal = Animal.objects.first()
        url = reverse('vaccine_new', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_vaccine_new_url_resolves_vaccine_new_view(self):
        view = resolve('/service/vaccine/new/1/')
        self.assertEquals(view.func, vaccine_new)

    def test_vaccine_list_status_code(self):
        animal = Animal.objects.first()
        url = reverse('vaccine_list', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_vaccine_list_url_resolves_vaccine_list_view(self):
        view = resolve('/service/vaccine/list/1/')
        self.assertEquals(view.func, vaccine_list)

    def test_vaccine_update_status_code(self):
        vaccine = Vaccine.objects.first()
        url = reverse('vaccine_update', args=(vaccine.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/vaccine_view_or_update.html')

    def test_vaccine_update_url_resolves_vaccine_update_view(self):
        view = resolve('/service/vaccine/edit/1/')
        self.assertEquals(view.func, vaccine_update)

    def test_create_vaccine(self):
        animal = Animal.objects.first()
        vaccine_type = VaccineType.objects.create(name='Gripe', price='0')
        vaccine = Vaccine.objects.create(animal=animal, date=datetime.date.today(), vaccine_type=vaccine_type)
        self.assertTrue(isinstance(vaccine_type, VaccineType))
        self.assertTrue(isinstance(vaccine, Vaccine))
        self.assertEqual(vaccine_type.__str__(), vaccine_type.name)

    def test_exam_new_status_code(self):
        animal = Animal.objects.first()
        url = reverse('exam_new', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_exam_new_url_resolves_exam_new_view(self):
        view = resolve('/service/exam/new/1/')
        self.assertEquals(view.func, exam_new)

    def test_exam_list_status_code(self):
        animal = Animal.objects.first()
        url = reverse('exam_list', args=(animal.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal/animal_tabs.html')

    def test_exam_list_url_resolves_exam_list_view(self):
        view = resolve('/service/exam/list/1/')
        self.assertEquals(view.func, exam_list)

    def test_exam_update_status_code(self):
        exam = Exam.objects.first()
        url = reverse('exam_update', args=(exam.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/exam_view_or_update.html')

    def test_exam_update_url_resolves_exam_update_view(self):
        view = resolve('/service/exam/edit/1/')
        self.assertEquals(view.func, exam_update)

    def test_create_exam(self):
        animal = Animal.objects.first()
        exam_category = ExamCategory.objects.create(name='Microbiologia')
        exam_type = ExamType.objects.create(name='Cultura para fungo', price='0', category=exam_category)
        exam = Exam.objects.create(animal=animal, date=datetime.date.today())
        exam.exam_type.add(exam_type)
        self.assertTrue(isinstance(exam_category, ExamCategory))
        self.assertTrue(isinstance(exam_type, ExamType))
        self.assertTrue(isinstance(exam, Exam))
        self.assertEqual(exam_category.__str__(), exam_category.name)
        self.assertEqual(exam_type.__str__(), exam_type.name)

    def test_exam_path(self):
        animal = Animal.objects.first()
        exam = Exam.objects.first()
        filename = 'exam.pdf'
        path = 'exams/{0}/{1}/{2}'.format(animal.animal_name, datetime.date.today().strftime('%d-%m-%Y'), filename)
        created_path = exam_path(exam, filename)
        self.assertEqual(path, created_path)


    # #
    # # Testing forms
    # #

    def test_valid_consultation_form(self):
        data = {'consultation_type': 1, 'date': datetime.date.today(), 'title': 'Lorem ipsum' }
        form = ConsultationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_animal_form(self):
        """
        Using empty date
        """
        data = {'consultation_type': 1, 'date': '', 'title': 'Lorem ipsum'}
        form = ConsultationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_vaccine_form(self):
        data = {'vaccine_type': 1, 'date': datetime.date.today()}
        form = VaccineForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_vaccine_form(self):
        """
        Using empty date
        """
        data = {'vaccine_type': 1, 'date': ''}
        form = VaccineForm(data=data)
        self.assertFalse(form.is_valid())

    # def test_valid_exam_form(self):
    #     data = {'date': datetime.date.today()}
    #     form = ExamForm(data=data)
    #     self.assertTrue(form.is_valid())

    def test_invalid_exam_form(self):
        """
        Using empty date
        """
        data = {'date': ''}
        form = ExamForm(data=data)
        self.assertFalse(form.is_valid())
