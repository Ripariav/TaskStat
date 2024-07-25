from django.shortcuts import render

# Create your views here.
def task_view(request):
    return render(request, 'dashboard/task.html')

def create_task_view(request):
    return render(request, 'dashboard/createtask.html')


