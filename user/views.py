from django.shortcuts import get_object_or_404, redirect, render
from .models import User
from .models import Log,Permission
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout as auth_logout
from datetime import datetime, timedelta
from django.utils import timezone


# Create your views here.
def check_login_decorator(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('/setting/login_warn')
        else:
            user = User.objects.get(id=request.session['user_id'])  # fetch user's info from User model
            permission_mapping = {
                1: "Manager",
                2: "Employee",
                3: "IT Administrator",
            }
            user_permission_name = permission_mapping.get(user.permission_id)
            # Find the permission with the specified permission_id and menu_id=5
            permission = Permission.objects.get(permission=user_permission_name, menu_id=5)
            if permission.position_id == 0:
                return redirect('/setting/warn')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@check_login_decorator
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

@check_login_decorator
def edit(request, userId):

    user = User.objects.get(id=userId)

    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        re_pass_word = request.POST.get('re_pass_word')
        permission_id = request.POST.get('permission')

        user.user_name = user_name
        user.permission_id = permission_id

        if pass_word != '' and pass_word == re_pass_word:
            user.pass_word = make_password(pass_word)

        user.save()
        user_id = request.session.get('user_id')
        operation_details = "user_edit "+ "user_id:"+str(userId)

        if user_id:
            Log.create_log(user_id, operation_details)
            return redirect('/user')

    context = {'user': user}
    return render(request, 'edit.html', context)

@check_login_decorator
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

        user_id = request.session.get('user_id')
        operation_details = "user_add"

        if user_id:
            Log.create_log(user_id, operation_details)

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

@check_login_decorator
def permission(request):
    return render(request, 'permission.html')

@check_login_decorator
def user_del(request, userId):
    user = get_object_or_404(User, id=userId)
    user.is_delete = 1
    user.save()

    user_id = request.session.get('user_id')
    operation_details = "user_del "+"user_id:"+str(userId)

    if user_id:
        Log.create_log(user_id, operation_details)

    return redirect('/user/')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(user_name=username)
        except User.DoesNotExist:
            # Render the form again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid username'})

        if user.is_locked:
            if user.locked_at and timezone.now() >= user.locked_at + timedelta(minutes=1):
                user.is_locked = False
                user.login_attempts = 0
                user.locked_at = None
                user.save()
            else:
                return render(request, 'login.html', {'error_message': 'Account is locked(1 minute). Please try again later.'})

        # Validate the password using Django's check_password function
        if check_password(password, user.pass_word):
            # Password is valid. Update the login state and redirect to success page
            user.login_attempts = 0
            user.is_locked = False
            user.save()

            # Store the user id in the session
            request.session['user_id'] = user.id
            request.session['username'] = username

            # Redirect to success page
            return redirect('/')
        else:
            user.login_attempts += 1
            if user.login_attempts >= 3:
                user.is_locked = True
                user.locked_at = timezone.now()
            user.save()
            # Render the form again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid password'})
    else:
        return render(request, 'login.html')


def wap_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(user_name=username)
        except User.DoesNotExist:
            return render(request, 'wap_login.html', {'error_message': 'Invalid username'})
      
        if check_password(password, user.pass_word):
            request.session['user_id'] = user.id
            request.session['username'] = username

            # Redirect to success page
            return redirect('/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid password'})
    else:
        return render(request, 'wap_login.html')

def logout(request):
    # This will remove the authenticated user's ID from the session
    auth_logout(request)

    # Then redirect to a success page or the home page
    return redirect('/')


def wap_logout(request):
    # This will remove the authenticated user's ID from the session
    auth_logout(request)

    # Then redirect to a success page or the home page
    return redirect('/user/wap/login')

@check_login_decorator
def logs(request, userId):
    query = request.GET.get('query')
    search_display = 1

    if userId == 0:
        log_data = Log.objects.filter(is_delete=0)
    else:
        search_display = 0
        log_data = Log.objects.filter(is_delete=0, user_id=userId)

    if query:
        log_data = log_data.filter(
            operation_details__icontains=query
        )


    paginator = Paginator(log_data.order_by(
            'id'), 10)  # 按照id字段升序排序
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'logs.html', {'page_obj': page_obj, 'query': query,'search_display':search_display})
