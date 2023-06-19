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
        permission_id = 3

        # Create a new User object with the form data
        user = User(
            user_name=user_name,
            pass_word=make_password(pass_word),
            permission_id=permission_id,
        )

        # Save the User object to the database
        user.save()

        # Redirect to the staff list page
        return redirect('/user/')

    else:
        # Render the staff_add.html template
        return render(request, 'add.html')


def permission(request):
    return render(request, 'permission.html')


def logs(request):
    return render(request, 'logs.html')


def login(request):
    return render(request, 'login.html')
