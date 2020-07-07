from django.db import models


class Link(models.Model):
    link_name = models.CharField(max_length=1000, blank=False)
    address = models.CharField(max_length=1000, blank=False)

    # def __str__(self):
    #     return self.name
