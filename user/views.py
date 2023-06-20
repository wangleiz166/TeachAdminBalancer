from django.shortcuts import get_object_or_404, redirect, render
from .models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.hashers import make_password

# Create your views here.


def list(request):
    query = request.GET.get('query')
    user_data = User.objects.filter(is_delete=0)

    if query:
        user_data = user_data.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    paginator = Paginator(user_data.order_by('id'), 10)  # 按照id字段升序排序
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'user_list.html', {'page_obj': page_obj, 'query': query})


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
    return render(request, 'login.html')
