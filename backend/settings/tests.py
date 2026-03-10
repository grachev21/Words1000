from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")  # Замените 'register' на имя вашего URL
        self.valid_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
        }

    def test_user_registration(self):
        # Проверяем, что пользователя еще нет в базе
        self.assertFalse(User.objects.filter(username="testuser").exists())

        # Отправляем POST-запрос на регистрацию
        response = self.client.post(self.register_url, data=self.valid_data)

        # Проверяем, что пользователь был создан
        self.assertTrue(User.objects.filter(username="testuser").exists())

        # Проверяем редирект после успешной регистрации
        # (замените 'home' на ваш URL для редиректа)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))
