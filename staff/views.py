from django.shortcuts import render

# Create your views here.
def staff_list(request):
    return render(request, 'staff_list.html')
