"""
URL configuration for hospitalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.show,name='base'),
    path('home',views.homes,name='home'),
    path('about',views.aboutus,name='about'),
    # path('booking',views.booking,name='booking'),
    # path('doctors',views. doctors_list,name='doctors'),
    # path('department',views.Department,name='department'),
    path('contact',views.contactus,name='contact'),
    path('form',views.displayfunction,name='form'),
    path('content',views.showmsg,name='content'),
    path('bookingform',views.form,name='bookingform')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

