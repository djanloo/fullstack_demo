from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Project

def index(request):
    if request.method == 'POST':
        Project.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
        )
        return redirect('/')
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})