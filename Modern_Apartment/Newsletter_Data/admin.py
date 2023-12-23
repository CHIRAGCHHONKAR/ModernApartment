from django.contrib import admin
from Newsletter_Data.models import Newsletter

class Newsletter_admin(admin.ModelAdmin):
    list_display=['Email']

admin.site.register(Newsletter,Newsletter_admin)    
# Register your models here.
