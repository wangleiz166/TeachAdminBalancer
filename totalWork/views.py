from django.shortcuts import render

# Create your views here.
def total_work_list(request):
    return render(request, 'total_work_list.html')

def total_work_detail(request):
    return render(request, 'total_work_detail.html')

def total_work_add(request):
    return render(request, 'total_work_add.html')

def total_work_bulk_add(request):
    return render(request, 'total_work_bulk_add.html')