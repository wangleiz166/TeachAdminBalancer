from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'list.html')

def detail(request):
    return render(request, 'detail.html')

