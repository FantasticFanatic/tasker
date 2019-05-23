from django.shortcuts import render, redirect
from .models import Task

def home_page(request):
    return render( request, 'home.html', {
        'tasks': Task.objects.all()
    })

def add_task_page(request):
    if request.method == "POST":
        title = request.POST['task_title']
        Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'add_task.html')