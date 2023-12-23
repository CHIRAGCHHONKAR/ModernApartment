from django.db import models



class feedback(models.Model):
    Client_Image=models.FileField(upload_to="Testimonials",default=None)
    Client_feedback=models.TextField()
    
    def __str__(self):
        return self.Client_feedback
# Create your models here.
