from django.shortcuts import render,redirect
from user.models import Permission,Log,User
from django.db import transaction

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
            # Find the permission with the specified permission_id and menu_id=6
            permission = Permission.objects.get(permission=user_permission_name, menu_id=6)
            if permission.position_id == 0:
                return redirect('/setting/warn')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Create your views here.
@check_login_decorator
def list(request):
    return render(request, 'setting_list.html')

def warn(request):
    return render(request, 'warn.html')

def login_warn(request):
    return render(request, 'login_warn.html')

@check_login_decorator
def permission_edit(request, permissionName):
    if request.method == 'POST':
        # Use transactions to guarantee the atomicity of all update operations
        with transaction.atomic():
            # Handling each permission
            for i in range(1, 7):
                # A position_id of 1 means selected, 0 means unselected.
                position_id = 1 if f'menu{i}_view' in request.POST else 0
                
                # Find records that meet the conditions and update them
                permission = Permission.objects.get(user_id=0, permission=permissionName, menu_id=i)
                permission.position_id = position_id
                permission.save()
        
        user_id = request.session.get('user_id')
        operation_details = "permission_edit "
                
        if user_id:
            Log.create_log(user_id, operation_details)

        # Redirect to the appropriate page
        return redirect('/setting/')

    permissions = Permission.objects.filter(user_id=0, permission=permissionName).values()
    permissions_dict = {f'menu{p["menu_id"]}_view': p["position_id"] for p in permissions}

    return render(request, 'permission_setting.html', {'permissions': permissions_dict,'permissionName':permissionName})

@check_login_decorator
def menu_edit(request):
    return render(request, 'menu_edit.html')
