from django.contrib import admin
from Property_Data.models import property

class property_admin(admin.ModelAdmin):
    list_display=["Property_category","Property_Description","Property_location","Property_price","Property_area","Property_images"]


admin.site.register(property,property_admin)
# Register your models here.


