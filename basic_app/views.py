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

    # if request.method == 'POST':
    #     user_form = UserForm(data=request.POST)
    #     profile_form = UserProfileInfoForm(data=request.POST)

    #     if user_form.is_valid() and profile_form.is_valid():

    #         user = user_form.save()

    #         user.set_password(user.password)
    #         user.save()

    #         profile = profile_form.save(commit=False)
    #         profile.user = user

    #         if 'profile_pic' in request.FILES:
    #             profile.profile_pic = request.FILES['profile_pic']

    #         profile.save()

    #         registered = True

    #     else:
    #         print(user_form.errors, profile_form.errors)

    # else:
    #     user_form = UserForm()
    #     profile_form = UserProfileInfoForm()
