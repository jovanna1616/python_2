from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm, NewTodoForm
from .models import Todo

# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name="main/home.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You logged in with username {username}")
                return redirect("main:todos")
            else:
                messages.error(request, f"Login attempt for username {username} failed.")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm
    return render(request=request,
                  template_name="main/auth/login.html",
                  context={"form": form})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get("username")
            messages.info(request, f"You registered and logged in with username {username}")
            return redirect("main:todos")
        else:
            for message in form.error_messages:
                message.error(request, f"{message}: {form.error_messages[message]}")
    
    form = NewUserForm
    return render(request=request,
                  template_name="main/auth/register.html",
                  context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")
                                    
                                    

def todos(request):
    form = NewTodoForm()
    if request.method == "POST":
        # set data
        form = NewTodoForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data["title"]
            messages.info(request, f"You created new todo with title {title}")
        return redirect("main:todos")

    return render(request=request,
                  template_name="main/todos.html",
                  context={"todos": Todo.objects.all().order_by("-created_at"), "form": form})

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = NewTodoForm(instance=todo)
    if request.method == "POST":
        form = NewTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            title = form.cleaned_data["title"]
            messages.info(request, f"You updated todo with title {title}")
            return redirect("main:todos")
    
    return render(request=request,
                   template_name="main/update-todo.html",
                   context={"form": form})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        todo.delete()
        messages.info(request, f"You updated todo with title {todo.title}")
        return redirect("main:todos")
    return render(request=request,
                   template_name="main/delete.html",
                   context={"todo": todo})