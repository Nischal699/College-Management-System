from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    topic=models.CharField(max_length=40)
    message=models.TextField()
