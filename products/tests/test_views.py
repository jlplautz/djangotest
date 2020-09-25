from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from mixer.backend.django import mixer
from django.test import TestCase
import pytest
from products.views import product_detail


@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Esta função via criar um setup:
        - esta é uma subclass do TestCase que vai garantir o acesso a metodos
          chamados setup class. E tudo que for inserido nesta function será chamada
          toda vez que outras funções
        :return:
        """
        super(TestViews, cls).setUpClass()
        mixer.blend('products.Product')
        cls.factory = RequestFactory()

    def test_product_detail_authenticated(self):
        path = reverse('detail', kwargs={'pk': 1})
        request = self.factory.get(path)
        request.user = mixer.blend(User)

        response = product_detail(request, pk=1)
        assert response.status_code == 200

    def test_product_detail_unauthenticated(self):
        path = reverse('detail', kwargs={'pk': 1})
        request = self.factory.get(path)
        request.user = AnonymousUser()

        response = product_detail(request, pk=1)
        assert 'accounts/login' in response.url
