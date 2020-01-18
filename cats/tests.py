"""Cat app tests"""

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse_lazy

from .models import Cat


class CatCase(TestCase):
    """Tests for cats"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='prueba123',
            email='prueba@gmail.com',
            password='contraseñaSegura123'
        )
        self.cat = Cat.objects.create(
            name='Gato de Prueba',
            breed='prueba',
            age=10,
            birthday=timezone.now(),
            owner=self.user
        )
        self.index = reverse_lazy('gatitos')
        self.create_cat = reverse_lazy('create_cat')

    def test_index(self):
        res = self.client.get(self.index)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Gato de Prueba', res.content)

    def test_cat_in_index(self):
        res = self.client.get(self.index)
        self.assertIn(b'Gato de Prueba', res.content)

    def test_create_cat(self):
        self.client.login(username='prueba123', password='contraseñaSegura123')
        res = self.client.get(self.index)
        self.assertNotIn(b'Otro Gato', res.content)
        self.client.post(self.create_cat, {
            'name': 'Otro Gato',
            'breed': 'gato',
            'age': 10
        })
        res = self.client.get(self.index)
        self.assertIn(b'Otro Gato', res.content)
