from django.db import models


class team(models.Model):
    Images=models.FileField(upload_to='Team',default=None)
    Name=models.CharField(max_length=100)
    PhoneNo=models.CharField(max_length=20)
    Email=models.EmailField()
    Facebook=models.URLField()
    Twitter=models.URLField()
    Linkedin=models.URLField()
    Instagram=models.URLField()
    
    def __str__(self):
        return self.Name
# Create your models here.
