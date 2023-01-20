from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy
from login_app.forms import UserRegisterForm
from django.contrib.auth.views import LogoutView

# Create your views here.

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='login.html',
        context={'form': form},
    )

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()  # Esto lo puedo usar porque es un model form
            success_url = reverse('inicio')
            return redirect(success_url)
    else:  # GET
        form = UserRegisterForm()
    return render(
        request=request,
        template_name='register.html',
        context={'form': form},
    )

def home(request):
    return render(
        request=request,
        template_name='panel.html',
    )

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'