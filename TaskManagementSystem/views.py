from django.shortcuts import render
from tasks.models import Task

def home(request):
    data = Task.objects.all()
    print(data)
    return render(request, 'home.html', {'data' : data})