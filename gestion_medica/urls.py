from django.urls import path
from .views import home, create_specialty, create_doctor, create_patient

urlpatterns = [
    path('', home, name='home'),
    path('nueva-especialidad/', create_specialty, name='create_specialty'),
    path('nuevo-doctor/', create_doctor, name='create_doctor'),
    path('nuevo-paciente/', create_patient, name='create_patient'),
]
