from django.contrib import admin

from django.contrib import admin
from .models import Doctor, Paciente, HistoriaClinica

admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(HistoriaClinica)

