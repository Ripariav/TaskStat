from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import TaskForm, CustomUserChangeForm, CustomPasswordChangeForm
from .models import Task
from datetime import datetime, timedelta
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.utils.timezone import now
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from datetime import datetime
import calendar

@login_required
def task_view(request):
    user = request.user
    priority_mapping = {'high': 1, 'medium': 2, 'low': 3}

    tasks = Task.objects.filter(user=user)
    tasks = sorted(tasks, key=lambda task: priority_mapping.get(task.priority, 4))
    tomorrow = Task.objects.filter(due_date=datetime.now().date() + timedelta(days=1))
    # tomorrow = sorted(tasks, key=lambda task: priority_mapping.get(task.priority, 4))
    today = Task.objects.filter(due_date=datetime.now().date())
    # today = sorted(tasks, key=lambda task: priority_mapping.get(task.priority, 4))
    
    active_tab = 1 

    task_events = [
        {
            'title': task.title,
            'start': task.due_date.strftime('%Y-%m-%d'),
            'url': reverse('update_task', args=[task.id])
        }
        for task in tasks
    ]

    context = {
        'user': user,
        'tasks': tasks,
        'tomorrow': tomorrow,
        'task_events': json.dumps(task_events, cls=DjangoJSONEncoder),
        'today': today,
        'active_tab': active_tab,
    }
    return render(request, 'dashboard/task.html', context)
        

@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Asignar el usuario actual al campo `user`
            task.save()
            return redirect('task')  # Redirige a una lista de tareas o a donde prefieras
    else:
        form = TaskForm()

    context = {
        'form': form,
        'user': request.user,
    }

    return render(request, 'dashboard/createtask.html', context)


@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
            form = TaskForm(instance=task)    
    
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'dashboard/updatetask.html', context)

@login_required
def statistics_view(request):
    user = request.user
    
    # Obtener todas las tareas del usuario
    tasks = Task.objects.filter(user=user)
    
    # Contar las tareas completadas y pendientes
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='completed').count()
    pending_tasks = tasks.filter(status__in=['pending', 'in_progress']).count()
    overdue_tasks = tasks.filter(due_date__lt=now().date()).count()

    # Obtener el mes y año actual
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year

    # Obtener el número de días en el mes actual
    days_in_month = calendar.monthrange(current_year, current_month)[1]
    days_labels = [day for day in range(1, days_in_month + 1)]

    active_tab = 2 

    # Bar chart data
    bar_data = {
        'labels': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
        'completed': [tasks.filter(status='completed', updated_at__week_day=i).count() for i in range(2, 9)]
    }

    # Line chart data
    line_data = {
        'labels': days_labels,
        'completed': [tasks.filter(status='completed', updated_at__year=current_year, updated_at__month=current_month, updated_at__day=day).count() for day in days_labels]
    }

    # Pie chart data
    pie_data = [
        {'value': tasks.filter(status='pending').count(), 'name': 'Pending'},
        {'value': tasks.filter(status='in_progress').count(), 'name': 'In Progress'},
        {'value': tasks.filter(status='completed').count(), 'name': 'Completed'}
    ]
    
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
        'bar_data': json.dumps(bar_data),
        'line_data': json.dumps(line_data),
        'pie_data': json.dumps(pie_data),
        'active_tab': active_tab,
    }
    
    return render(request, 'dashboard/stats.html', context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Actualizar la sesión para que el usuario no sea desconectado
            return redirect('profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    active_tab = 3
    
    context = {
        'user_form': user_form,
        'password_form': password_form,
        'active_tab': active_tab,
    }
    return render(request, 'dashboard/profile.html', context)


def update_profile_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    
    user = request.user
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'dashboard/profile.html', context)