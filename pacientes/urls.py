from django.urls import path
from .views import (
    DoctorListView,
    DoctorDetailView,
    DoctorCreateView,
    DoctorUpdateView,
    DoctorDeleteView,
)

urlpatterns = [
    path('doctores/', DoctorListView.as_view(), name='doctor_list'),
    path('doctores/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctores/nuevo/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctores/<int:pk>/editar/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/<int:pk>/eliminar/', DoctorDeleteView.as_view(), name='doctor_delete'),

]
