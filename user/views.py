from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'user_list.html')

def edit(request):
    return render(request, 'edit.html')

def add(request):
    return render(request, 'add.html')

def permission(request):
    return render(request, 'permission.html')

def logs(request):
    return render(request, 'logs.html')