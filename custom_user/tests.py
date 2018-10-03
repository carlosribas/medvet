from django.apps import apps
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.core.urlresolvers import reverse, resolve
from django.test import TestCase
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from custom_user.apps import CustomUserConfig
from custom_user.views import *

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


class PasswordResetTests(TestCase):
    def setUp(self):
        url = reverse('password_reset')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/reset/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, PasswordResetForm)

    def test_form_inputs(self):
        """
        The view must contain two inputs: csrf and email
        """
        self.assertContains(self.response, '<input', 2)
        self.assertContains(self.response, 'type="email"', 1)


class InvalidPasswordResetTests(TestCase):
    def setUp(self):
        url = reverse('password_reset')
        self.response = self.client.post(url, {'email': 'donotexist@email.com'})

    def test_redirection(self):
        """
        Even invalid emails in the database should
        redirect the user to `password_reset_done` view
        """
        url = reverse('password_reset_done')
        self.assertRedirects(self.response, url)

    def test_no_reset_email_sent(self):
        self.assertEqual(0, len(mail.outbox))


class PasswordResetDoneTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_done')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/reset/done/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetDoneView)


class PasswordResetConfirmTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email='john@doe.com', password='123abcdef')

        """
        create a valid password reset token
        based on how django creates the token internally:
        https://github.com/django/django/blob/1.11.5/django/contrib/auth/forms.py#L280
        """
        self.uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        self.token = default_token_generator.make_token(user)

        url = reverse('password_reset_confirm', kwargs={'uidb64': self.uid, 'token': self.token})
        self.response = self.client.get(url, follow=True)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/reset/{uidb64}/{token}/'.format(uidb64=self.uid, token=self.token))
        self.assertEquals(view.func.view_class, auth_views.PasswordResetConfirmView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SetPasswordForm)

    def test_form_inputs(self):
        """
        The view must contain two inputs: csrf and two password fields
        """
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, 'type="password"', 2)


class InvalidPasswordResetConfirmTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email='john@doe.com', password='123abcdef')
        uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        token = default_token_generator.make_token(user)

        """
        invalidate the token by changing the password
        """
        user.set_password('abcdef123')
        user.save()

        url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_html(self):
        password_reset_url = reverse('password_reset')
        self.assertContains(self.response, 'invalid password reset link')
        self.assertContains(self.response, 'href="{0}"'.format(password_reset_url))


class PasswordResetCompleteTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_complete')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/reset/complete/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetCompleteView)


class PasswordChangeTestCase(TestCase):
    def setUp(self, data={}):
        self.user = User.objects.create_user(username='john', email='john@doe.com', password='old_password')
        self.url = reverse('password_change')
        self.client.login(username='john', password='old_password')
        self.response = self.client.post(self.url, data)

class ReportsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(CustomUserConfig.name, 'custom_user')
        self.assertEqual(apps.get_app_config('custom_user').name, 'custom_user')


class CustomUserTest(TestCase):
    def setUp(self):
        """
        Configure authentication and variables to start each test
        """

        self.user = User.objects.create_user(username=USER_USERNAME, email=USER_EMAIL, password=USER_PWD)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

        logged = self.client.login(username=USER_USERNAME, password=USER_PWD)
        self.assertEqual(logged, True)

    def test_user_list_view_status_code(self):
        url = reverse('user_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_user/user_list.html')

    def test_user_list_url_resolves_user_list_view(self):
        view = resolve('/custom_user/search')
        self.assertEquals(view.func, user_list)

    def test_new_user_view_status_code(self):
        url = reverse('new_user')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_user/register_users.html')

    def test_new_user_url_resolves_new_user_view(self):
        view = resolve('/custom_user/new/')
        self.assertEquals(view.func, new_user)

    def test_new_user(self):
        url = reverse('new_user')
        self.data = {
            'first_name': 'Fulano',
            'last_name': 'de Tal',
            'username': 'fulano',
            'email': 'fulano@example.com',
            'password1': 'abc123',
            'password2': 'abc123',
            'action': 'save'
        }
        self.client.post(url, self.data)
        user = User.objects.filter(username='fulano')
        self.assertEqual(user.count(), 1)

    def test_new_user_invalid_form(self):
        url = reverse('new_user')
        self.data = {
            'first_name': 'Fulano',
            'last_name': 'de Tal',
            'username': 'fulano',
            'email': 'fulano',
            'password1': 'abc123',
            'password2': 'abc123',
            'action': 'save'
        }
        response = self.client.post(url, self.data)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue("Information not saved." in message.message)

    def test_update_user_view_status_code(self):
        url = reverse('update_user', args=(self.user.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_user/register_users.html')

    def test_update_user_url_resolves_update_user_view(self):
        view = resolve('/custom_user/edit/1/')
        self.assertEquals(view.func, update_user)

    def test_update_user(self):
        self.data = {
            'first_name': 'Fulano',
            'last_name': 'de Tal',
            'username': USER_USERNAME,
            'email': USER_EMAIL,
            'password1': USER_PWD,
            'password2': USER_PWD,
            'action': 'save'
        }
        response = self.client.post(reverse("update_user", args=(self.user.id,)), self.data)
        self.assertEqual(response.status_code, 302)

    def test_remove_user(self):
        self.data = {
            'action': 'remove'
        }
        response = self.client.post(reverse("update_user", args=(self.user.id,)), self.data)
        self.assertEqual(response.status_code, 302)
        user = User.objects.first()
        self.assertFalse(user.is_active)
