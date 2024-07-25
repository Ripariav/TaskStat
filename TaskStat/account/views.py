from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task')
    else:
        form = AuthenticationForm()

    return render(request, 'account/login.html', {
        'form': form,
        'error': form.errors
        })

def signup_view(request):
    # Check if it is POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # Get data
        if form.is_valid():
            #save.
            form.save()
            return redirect('task')
    else:
        # otherwise, if is not rigth the de form we'll recreate it.
        form = UserCreationForm()
#just show the web. 
    return render(request,'account/signup.html', {
        'form': UserCreationForm,
        'error': form.errors,
    })

def logout_view(request):
    logout(request)
    return redirect('main')