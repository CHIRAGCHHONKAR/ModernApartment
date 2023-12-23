from django.contrib import admin
from Testimonials.models import feedback

class feedback_admin(admin.ModelAdmin):
    list_display=['Client_feedback','Client_Image']
    
admin.site.register(feedback,feedback_admin)    
# Register your models here.
