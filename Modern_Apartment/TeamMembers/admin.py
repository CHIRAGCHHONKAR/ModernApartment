from django.contrib import admin
from TeamMembers.models import team

class team_admin(admin.ModelAdmin):
    list_display=['Name','PhoneNo','Email','Facebook','Twitter','Linkedin','Instagram','Images']
    
admin.site.register(team,team_admin)    
# Register your models here.
