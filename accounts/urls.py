from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('change-password/',
         auth_views.PasswordChangeView.as_view(
             template_name='accounts/change_password.html',
             success_url='/accounts/profile/'
         ),
         name='change_password'),
]

