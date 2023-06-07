from django.shortcuts import render

# Create your views here.
def staff_list(request):
    return render(request, 'staff_list.html')

def staff_add(request):
    return render(request, 'staff_add.html')

def staff_bulk_add(request):
    return render(request, 'staff_bulk_add.html')

def staff_detail(request):
    return render(request, 'staff_detail.html')
