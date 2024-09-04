
from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class CustomUserChangeForm(UserChangeForm):
    password = None  # No mostrar el campo de la contraseña

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')  # Solo estos campos

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('password',)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=Task.STATUS_CHOICES),
            'priority': forms.Select(choices=Task.PRIORITY_CHOICES),
        }
