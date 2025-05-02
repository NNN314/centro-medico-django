from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pacientes.models import Doctor
from django.urls import reverse_lazy
from .models import Doctor

class DoctorListView(ListView):
    model = Doctor
    template_name = "pacientes/doctor_list.html"  # Asegúrate de que esta ruta sea correcta
    context_object_name = "doctores"

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "pacientes/doctor_detail.html"
    context_object_name = "doctor"

class DoctorCreateView(CreateView):
    model = Doctor
    fields = ['nombre', 'especialidad', 'telefono', 'email']
    template_name = "pacientes/doctor_form.html"
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ['nombre', 'especialidad', 'telefono', 'email']
    template_name = "pacientes/doctor_form.html"
    success_url = reverse_lazy('doctor_list')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = "pacientes/doctor_confirm_delete.html"
    success_url = reverse_lazy('doctor_list')


