from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cita

class CitaListView(ListView):
    model = Cita
    template_name = "citas/cita_list.html"  # Ubicación de la plantilla
    context_object_name = "citas"

class CitaDetailView(DetailView):
    model = Cita
    template_name = "citas/cita_detail.html"
    context_object_name = "cita"

class CitaCreateView(CreateView):
    model = Cita
    fields = ['paciente', 'doctor', 'fecha', 'hora', 'mensaje']  # Puedes personalizar los campos
    template_name = "citas/cita_form.html"
    success_url = reverse_lazy('cita_list')

class CitaUpdateView(UpdateView):
    model = Cita
    fields = ['paciente', 'doctor', 'fecha', 'hora', 'mensaje']
    template_name = "citas/cita_form.html"
    success_url = reverse_lazy('cita_list')

class CitaDeleteView(DeleteView):
    model = Cita
    template_name = "citas/cita_confirm_delete.html"
    success_url = reverse_lazy('cita_list')
