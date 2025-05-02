from django.db import models

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre
    
class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    diagnostico = models.TextField()
    fecha_consulta = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Historia de {self.paciente.nombre} - {self.fecha_consulta}"


