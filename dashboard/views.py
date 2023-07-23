from django.shortcuts import render,redirect
from user.models import User,Permission

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
            # Find the permission with the specified permission_id and menu_id=4
            permission = Permission.objects.get(permission=user_permission_name, menu_id=4)
            if permission.position_id == 0:
                return redirect('/setting/warn')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@check_login_decorator
def dashboard(request):
    return render(request, 'dashboard.html')
