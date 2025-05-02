from django.contrib import admin
from .models import Specialty, Doctor, Patient

admin.site.register(Specialty)
admin.site.register(Doctor)
admin.site.register(Patient)
