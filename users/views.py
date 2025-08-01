from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

class UserLogin(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        # where to go after login in
        return reverse_lazy("home")
    

def logout_view(request):
    logout(request)
    return redirect('login')

