from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Mensaje

# Vista de la Bandeja de Entrada (Inbox): muestra los mensajes recibidos por el usuario autenticado
class InboxMessageListView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = "mensajes/inbox.html"
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user).order_by('-creado')

# Vista para ver el detalle de un mensaje
class MensajeDetailView(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = "mensajes/mensaje_detail.html"
    context_object_name = "mensaje"

# Vista para enviar un nuevo mensaje
class MensajeCreateView(LoginRequiredMixin, CreateView):
    model = Mensaje
    fields = ['destinatario', 'asunto', 'cuerpo']
    template_name = "mensajes/mensaje_form.html"
    success_url = reverse_lazy('inbox')  # Nombre de la URL de la Bandeja de Entrada

    def form_valid(self, form):
        # Asigna el usuario autenticado como remitente
        form.instance.remitente = self.request.user
        return super().form_valid(form)
