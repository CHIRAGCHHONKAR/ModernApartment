from django.db import models

class contactform(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()
# Create your models here.
