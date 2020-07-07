import factory

from .models import Link


class LinkModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Link
        