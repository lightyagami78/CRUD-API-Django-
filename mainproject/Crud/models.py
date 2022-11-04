from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()


# Create / insert / Add - GET
# Reterive / Fetch - Get
# Update/ Edit - POST
#Delete - Delete