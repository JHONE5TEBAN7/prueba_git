from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountFlowTests(TestCase):
    def test_login_and_registration_pages_render(self):
        self.assertEqual(self.client.get(reverse("home")).status_code, 200)
        self.assertEqual(self.client.get(reverse("login")).status_code, 200)
        self.assertEqual(self.client.get(reverse("register")).status_code, 200)

    def test_client_can_register_and_is_logged_in(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "cliente",
                "password1": "UnaClave-segura-739!",
                "password2": "UnaClave-segura-739!",
            },
        )

        self.assertRedirects(
            response, reverse("client_dashboard"), fetch_redirect_response=False
        )
        user = User.objects.get(username="cliente")
        self.assertFalse(user.is_staff)
        self.assertEqual(
            self.client.get(reverse("client_dashboard")).status_code, 200
        )

    def test_client_login_redirects_to_client_dashboard(self):
        User.objects.create_user(username="cliente", password="Clave-segura-739!")

        response = self.client.post(
            reverse("login"),
            {"username": "cliente", "password": "Clave-segura-739!"},
        )

        self.assertRedirects(
            response, reverse("client_dashboard"), fetch_redirect_response=False
        )

    def test_staff_login_redirects_to_admin(self):
        User.objects.create_superuser(
            username="administrador",
            email="admin@example.com",
            password="Clave-segura-739!",
        )

        response = self.client.post(
            reverse("login"),
            {"username": "administrador", "password": "Clave-segura-739!"},
        )

        self.assertRedirects(
            response, reverse("admin:index"), fetch_redirect_response=False
        )

    def test_client_dashboard_requires_authentication(self):
        response = self.client.get(reverse("client_dashboard"))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("login")))