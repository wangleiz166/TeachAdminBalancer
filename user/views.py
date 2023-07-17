from django.shortcuts import get_object_or_404, redirect, render
from .models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout as auth_logout


# Create your views here.


def list(request):
    query = request.GET.get('query')
    user_data = User.objects.filter(is_delete=0)

    if query:
        user_data = user_data.filter(

            user_name__icontains=query
        )

    paginator = Paginator(user_data.order_by(
        'permission_id'), 10)  # 按照id字段升序排序
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'user_list.html', {'page_obj': page_obj, 'query': query})


def edit(request):
    return render(request, 'edit.html')


def add(request):
    if request.method == 'POST':
        # Retrieve the form data from the request
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        permission_id = request.POST.get('permission_id')
        # Create a new User object with the form data
        user = User(
             user_name=user_name,
             pass_word=make_password(pass_word),
             permission_id=permission_id
        )

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(user_name=username)
        except User.DoesNotExist:
            # Render the form again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid username'})

        # Validate the password using Django's check_password function
        if check_password(password, user.pass_word):
            # Password is valid. Update the login state and redirect to success page
            user.is_login = True
            user.save()

            # Store the user id in the session
            request.session['user_id'] = user.id
            request.session['username'] = username
            
            # Redirect to success page
            return redirect('/')
        else:
            # Render the form again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid password'})
    else:
        return render(request, 'login.html')

def logout(request):
    # This will remove the authenticated user's ID from the session
    auth_logout(request)

    # Then redirect to a success page or the home page
    return redirect('/')