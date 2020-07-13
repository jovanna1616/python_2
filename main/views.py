from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name="main/home.html")

def login_request(request):
    return render(request=request,
                  template_name="main/auth/login.html")

def register_request(request):
    return render(request=request,
                  template_name="main/auth/register.html")

def logout_request(request):
    return render(request=request,
                  template_name="main/auth/logout.html")