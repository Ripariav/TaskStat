from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task

@login_required
def task_view(request):
    user =  request.user
    tasks = Task.objects.filter(user=user)
    context={
        'user': user,
        'tasks': tasks,
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


