from django.db import models


class property(models.Model):
    Category_Choice = (
        ('', 'category'),
        ('Commercial', 'Commercial'),
        ('Land', 'Land'),
        ('Vacation/Short-term Rentals', 'Vacation/Short-term Rentals'),
        ('Residential', 'Residential'),
        ('Plot', 'Plot'),
        ('Apartment', 'Apartment'),
    )
     
    Property_category = models.CharField(choices=Category_Choice, max_length=100, null=True)
    Property_Description = models.TextField()
    Property_location = models.TextField(default='India')
    Property_price = models.CharField(max_length=30,default=0.0)
    Property_area = models.CharField(max_length=30,default=0.0)
    Property_images = models.FileField(upload_to='properties')

# Create your models here.
