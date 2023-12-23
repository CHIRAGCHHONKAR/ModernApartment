from django.db import models


class Newsletter(models.Model):
    Email=models.EmailField(max_length=254)
# Create your models here.
