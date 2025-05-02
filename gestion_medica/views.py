from django.shortcuts import render, redirect
from pacientes.models import Doctor
from .forms import SpecialtyForm, DoctorForm, PatientForm
from .models import Doctor, Specialty, Patient

# Página de inicio que muestra una lista de doctores (puedes cambiar según preferencia)
def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})

# Vista para crear una nueva especialidad
def create_specialty(request):
    if request.method == 'POST':
        form = SpecialtyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SpecialtyForm()
    return render(request, 'create_specialty.html', {'form': form})

# Vista para crear un nuevo doctor
def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DoctorForm()
    return render(request, 'create_doctor.html', {'form': form})

# Vista para crear un nuevo paciente
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'create_patient.html', {'form': form})

from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def home(request):
    # Si deseas mostrar siempre el primer doctor (o algún doctor específico)
    doctor = Doctor.objects.first()  # O ajusta la lógica según tu requerimiento
    return render(request, 'gestion_medica/home.html', {'doctor': doctor})


