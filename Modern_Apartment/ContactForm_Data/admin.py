from django.contrib import admin
from ContactForm_Data.models import contactform

class admin_contactform(admin.ModelAdmin):
    list_display=['name','email','subject','message']
    
admin.site.register(contactform,admin_contactform)    
# Register your models here.
