
from django.urls import path
from .views import (
    CitaListView,
    CitaDetailView,
    CitaCreateView,
    CitaUpdateView,
    CitaDeleteView,
)

urlpatterns = [
    path('', CitaListView.as_view(), name='cita_list'),
    path('<int:pk>/', CitaDetailView.as_view(), name='cita_detail'),
    path('nueva/', CitaCreateView.as_view(), name='cita_create'),
    path('<int:pk>/editar/', CitaUpdateView.as_view(), name='cita_update'),
    path('<int:pk>/eliminar/', CitaDeleteView.as_view(), name='cita_delete'),
]
