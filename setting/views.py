from django.shortcuts import render,redirect
from user.models import Permission
from django.db import transaction

# Create your views here.
def list(request):
    return render(request, 'setting_list.html')



def permission_edit(request):
    if request.method == 'POST':
        # Use transactions to guarantee the atomicity of all update operations
        with transaction.atomic():
            # Handling each permission
            for i in range(1, 7):
                # A position_id of 1 means selected, 0 means unselected.
                position_id = 1 if f'menu{i}_view' in request.POST else 0
                
                # Find records that meet the conditions and update them
                permission = Permission.objects.get(user_id=0, permission='Manager', menu_id=i)
                permission.position_id = position_id
                permission.save()

        # Redirect to the appropriate page
        return redirect('/setting/')

    permissions = Permission.objects.filter(user_id=0, permission='Manager').values()
    permissions_dict = {f'menu{p["menu_id"]}_view': p["position_id"] for p in permissions}

    return render(request, 'permission_setting.html', {'permissions': permissions_dict})

def menu_edit(request):
    return render(request, 'menu_edit.html')