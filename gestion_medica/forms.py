from django import forms
from .models import Specialty, Doctor, Patient

# Formulario para la especialidad
class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialty
        fields = ['name', 'description']

# Formulario para el doctor
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'phone', 'email', 'available_hours']

# Formulario para el paciente
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'history', 'phone', 'email']
