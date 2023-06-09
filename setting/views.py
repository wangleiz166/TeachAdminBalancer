from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'setting_list.html')

def permission_edit(request):
    return render(request, 'permission_setting.html')

def menu_edit(request):
    return render(request, 'menu_edit.html')