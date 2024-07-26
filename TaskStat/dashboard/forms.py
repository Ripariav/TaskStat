
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=Task.STATUS_CHOICES),
            'priority': forms.Select(choices=Task.PRIORITY_CHOICES),
        }
