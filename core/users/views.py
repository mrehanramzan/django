from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login

from .forms import AuthenticateForm

def login_view(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")
        user = authenticate(request, email=email, password=password)    
        if user is not None:
            auth_login(request, user)
            return render(request, 'dashboard.html')
        else:
            print("Invalid credentials")
    return render(request, 'users/login.html')



def register_view(request):
    return render(request, 'users/signup.html')


def login_view_django(request):
    if request.method == 'POST':
        form = AuthenticateForm(request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return render(request, 'dashboard.html')
        else :
            context = {
            'forms':form
            }
            return render(request, 'users/login.html', context)
    else:
        context = {
            'forms':AuthenticateForm()
        }
        return render(request, 'users/login.html', context)