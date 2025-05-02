from django.db import models
from django.contrib.auth.models import User


from pacientes.models import Doctor

class Cita(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    mensaje = models.TextField(blank=True, null=True)
    creada = models.DateTimeField(auto_now_add=True)
    actualizada = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cita: {self.paciente.username} con Dr. {self.doctor.nombre} el {self.fecha} a las {self.hora}"
