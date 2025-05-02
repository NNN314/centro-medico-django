from django.urls import path
from .views import InboxMessageListView, MensajeDetailView, MensajeCreateView

urlpatterns = [
    path('inbox/', InboxMessageListView.as_view(), name='inbox'),
    path('enviar/', MensajeCreateView.as_view(), name='enviar_mensaje'),
    path('<int:pk>/', MensajeDetailView.as_view(), name='mensaje_detail'),
]
