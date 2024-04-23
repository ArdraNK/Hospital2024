from django.contrib import admin

from myapp.models import department, Doctors, Booking

# Register your models here.
admin.site.register(department)
admin.site.register(Doctors)
admin.site.register(Booking)
