from django.shortcuts import render, redirect

from .forms import UserForm, UserProfileInfoForm
# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    # registered = False
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():

            form.save()
        return redirect('http://127.0.0.1:8000/home')

    return render(request, 'basic_app/registration.html', {'form': form})
