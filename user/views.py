from django.shortcuts import get_object_or_404, redirect, render
from .models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.hashers import make_password

# Create your views here.


def list(request):
    return render(request, 'user_list.html')


def edit(request):
    return render(request, 'edit.html')


def add(request):
    if request.method == 'POST':
        # Retrieve the form data from the request
        user_name = request.POST.get('username')
        pass_word = request.POST.get('pass_word')
        permission_id = request.POST.get('permission_id')
        # Create a new User object with the form data
        user = User(
            user_name=user_name,
            pass_word=make_password(pass_word),
            permission_id=permission_id,
        )
<<<<<<< HEAD
        print(user.permission_id)
=======
      
>>>>>>> 72232cfe857a5ea5cc05903c17b555e55e26abb0
        # Save the User object to the database
        user.save()

        # Redirect to the staff list page
        return redirect('/user/')

    else:
        # Render the staff_add.html template
        return render(request, 'add.html')

# def staff_delete(request, staffId):
#     user = get_object_or_404(User, id=staffId)
#     user.is_delete = 1
#     user.save()
#     return redirect('user_list')


def permission(request):
    return render(request, 'permission.html')


def logs(request):
    return render(request, 'logs.html')


def login(request):
    return render(request, 'login.html')
