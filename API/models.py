from django.db import models

# Create your models here.
class Api(models.Model):
    experiences = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)
    addres = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title