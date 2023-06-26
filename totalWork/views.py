from django.shortcuts import render

# Create your views here.
def total_work_list(request):
    return render(request, 'total_work.html')

def admin_roles(request):
    return render(request, 'admin_roles.html')

def overall_calcs(request):
    return render(request, 'overall_calcs.html')

def frozen_modules(request):
    return render(request, 'frozen_modules.html')
