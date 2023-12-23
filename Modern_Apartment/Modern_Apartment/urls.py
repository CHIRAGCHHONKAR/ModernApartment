"""
URL configuration for Modern_Apartment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Modern_Apartment import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('about/',views.aboutpage),
    path('property/',views.propertypage,name='property'),
    path('contact/',views.contactpage),
    path('Contactform/',views.Contactform,name='Contactform'),
    path('login/',views.loginpage,name='loginpage'),
    path('signup/',views.signuppage,name='signuppage'),
    path('logout/',views.logoutpage,name='logout'),
    path('Newsletterdata/',views.Newsletterdata,name='Newsletterdata'),
    path('privacypolicy/',views.privacypolicy),
    path('termsofuse/',views.termsofuse),
    path('helpdesk/',views.helpdesk),
    path('searchresult/', views.searchresult,name='searchresult'),
    path('addproperty/',views.addproperty,name='addproperty'),
    path('Propertydata/',views.Propertydata,name='Propertydata'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('profilepage/',views.Profilepage,name='profilepage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
