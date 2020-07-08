from django.test import TestCase, Client
from django.urls import reverse

import factory
from .factories import LinkModelFactory


class LinkFactoryTestCase(TestCase):
    """Checks for valid model creation and attributes."""
    def test_200(self):
        link_factory = LinkModelFactory()
        self.assertIsNotNone(link_factory.address)
        self.assertIsNotNone(link_factory.link_name)


class ScapeHomeTestCase(TestCase):
    """Checks response for valid home page get request."""
    def test_200(self):
        url = reverse('home')
        client = Client()
        response = client.get(url)
        self.assertIs(response.status_code, 200) 


class ClearLinksTestCase(TestCase):
    """Checks response for valid delete endpoint request."""
    def test_200(self):
        url = reverse('clear_links')
        client = Client()
        response = client.delete(url)
        self.assertEqual(response.status_code, 302) 