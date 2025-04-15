from django.db import models

# Modelo para guardar especialidades médicas
class Specialty(models.Model):
    name = models.CharField(max_length=50)  # Nombre de la especialidad
    description = models.TextField(blank=True)  # Descripción opcional

    def __str__(self):
        return self.name

# Modelo para los doctores
class Doctor(models.Model):
    name = models.CharField(max_length=100)  # Nombre completo
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)  # Relación con el modelo Specialty
    phone = models.CharField(max_length=20, blank=True)  # Teléfono (opcional)
    email = models.EmailField(blank=True)  # Correo electrónico (opcional)
    available_hours = models.CharField(max_length=100, blank=True)  # Horarios disponibles

    def __str__(self):
        return self.name

# Modelo para los pacientes
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    history = models.TextField(blank=True)  # Historial médico (opcional)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name
