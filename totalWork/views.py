from django.shortcuts import render

# Create your views here.
def total_work_list(request):
    return render(request, 'total_work_list.html')