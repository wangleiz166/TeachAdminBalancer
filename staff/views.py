from django.shortcuts import get_object_or_404, redirect, render
from .models import Staff
from user.models import Log,User,Permission
from staffvModules.models import TeachCourse,TeachProject,TeachSchoolRoles,TeachAdminRole,TeachUniRoles
from django.core.paginator import Paginator
import datetime
from django.db.models import Q


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
            # Find the permission with the specified permission_id and menu_id=2
            permission = Permission.objects.get(permission=user_permission_name, menu_id=2)
            if permission.position_id == 0:
                return redirect('/setting/warn')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@check_login_decorator
def staff_list(request):
    query = request.GET.get('query')
    staff_data = Staff.objects.filter(is_delete=0)

    if query:
        staff_data = staff_data.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(initials__icontains=query)
        )


    paginator = Paginator(staff_data.order_by('id'), 10)  # 按照id字段升序排序
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'staff_list.html', {'page_obj': page_obj, 'query': query})

@check_login_decorator
def totalwork_h5(request, staffId):
    staff_first_name = Staff.objects.get(id=staffId).first_name
    staff_last_name = Staff.objects.get(id=staffId).last_name
    staff_name = staff_first_name + " " + staff_last_name
    staff_permitt_hours = Staff.objects.get(id=staffId).adjusted_max

    courses = TeachCourse.objects.raw("""
        SELECT * 
        FROM balancer_teach_course AS a 
        LEFT JOIN balancer_course AS b 
        ON a.course_name = b.code 
        WHERE b.is_delete = 0 and a.staff_id = %s
    """, [staffId])

    projects = TeachProject.objects.filter(staff_id=staffId).all()
    admin_roles = TeachAdminRole.objects.filter(staff_id=staffId).all()
    school_roles = TeachSchoolRoles.objects.filter(staff_id=staffId).all()
    uni_roles = TeachUniRoles.objects.filter(staff_id=staffId).all()

    courses_hours = sum([float(c.total_hours) for c in courses])
    projects_hours = sum([float(p.total_hours) for p in projects])
    admin_roles_hours = sum([float(a.total_hours) for a in admin_roles])
    school_roles_hours = sum([float(s.total_hours) for s in school_roles])
    uni_roles_hours = sum([float(u.total_hours) for u in uni_roles])

    staff_total_hours = courses_hours + projects_hours + admin_roles_hours +  school_roles_hours + uni_roles_hours
    staff_total_no_project_hours = courses_hours  + admin_roles_hours +  school_roles_hours + uni_roles_hours

    context =  {
                    'staff_name': staff_name,
                    'staff_permitt_hours':staff_permitt_hours,
                    'staff_total_hours':staff_total_hours,
                    'staff_total_no_project_hours':staff_total_no_project_hours,
                    'staff_total_hours_left': float(staff_permitt_hours) - staff_total_hours,
               }

    return render(request, 'total_work_h5.html', context)

@check_login_decorator
def staff_search(request):
    staff_data = Staff.objects.filter(is_delete=0)
    paginator = Paginator(staff_data, 10)  # Show 10 staff members per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'staff_list.html', {'page_obj': page_obj})

@check_login_decorator
def staff_delete(request, staffId):
    staff = get_object_or_404(Staff, id=staffId)
    staff.is_delete = 1
    staff.save()

    user_id = request.session.get('user_id')
    operation_details = "staff_delete "+ "user_id:"+str(staffId)
    
    if user_id:
        Log.create_log(user_id, operation_details)

    return redirect('staff_list')

@check_login_decorator
def staff_add(request):
    if request.method == 'POST':
        # Retrieve the form data from the request
        initials = request.POST.get('initials')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        cat = request.POST.get('cat')
        probation_year = request.POST.get('probation')
        annual_availability = request.POST.get('availability')
        unadjusted_max = request.POST.get('unadjustedMax')
        adjusted_max = request.POST.get('adjustedMax')
        availability_notes = request.POST.get('availabilityNotes')
        employment_end_date = request.POST.get('emplEndDate')
        probation_start_date = request.POST.get('probationStartDate')
        probation_start_year_stage = request.POST.get(
            'probationStartYearStage')

        # Create a new Staff object with the form data
        staff = Staff(
            initials=initials,
            first_name=first_name,
            last_name=last_name,
            cat=cat,
            probation_year=probation_year,
            annual_availability=annual_availability,
            unadjusted_max=unadjusted_max,
            adjusted_max=adjusted_max,
            availability_notes=availability_notes,
            employment_end_date=employment_end_date,
            probation_start_date=probation_start_date,
            probation_start_year_stage=probation_start_year_stage
        )

        # Save the Staff object to the database
        staff.save()
        
        user_id = request.session.get('user_id')
        operation_details = "staff_add "
        
        if user_id:
            Log.create_log(user_id, operation_details)

        # Redirect to the staff list page
        return redirect('/staff/')

    else:
        # Render the staff_add.html template
        return render(request, 'staff_add.html')

@check_login_decorator
def staff_bulk_add(request):
    return render(request, 'staff_bulk_add.html')

@check_login_decorator
def staff_detail(request, staffId):
    staff = get_object_or_404(Staff, id=staffId)
    return render(request, 'staff_detail.html', {'staff': staff})

@check_login_decorator
def staff_update(request, staffId):
    staff = get_object_or_404(Staff, id=staffId)

    staff.initials = request.POST.get('initials')
    staff.first_name = request.POST.get('firstName')
    staff.last_name = request.POST.get('lastName')
    staff.cat = request.POST.get('cat')
    staff.probation_year = request.POST.get('probation')
    staff.annual_availability = request.POST.get('availability')
    staff.unadjusted_max = request.POST.get('unadjustedMax')
    staff.adjusted_max = request.POST.get('adjustedMax')
    staff.availability_notes = request.POST.get('availabilityNotes')

    employment_end_date_str = request.POST.get('emplEndDate')
    if employment_end_date_str:
        employment_end_date = datetime.datetime.strptime(
            employment_end_date_str, '%b. %d, %Y')
        staff.employment_end_date = employment_end_date.date()

    probation_start_date_str = request.POST.get('probationStartDate')
    if probation_start_date_str:
        probation_start_date = datetime.datetime.strptime(
            probation_start_date_str, '%b. %d, %Y')
        staff.probation_start_date = probation_start_date.date()

    staff.probation_start_year_stage = request.POST.get(
        'probationStartYearStage')

    staff.save()

    user_id = request.session.get('user_id')
    operation_details = "staff_update "+ "user_id:"+str(staffId)
        
    if user_id:
        Log.create_log(user_id, operation_details)


    return redirect('/staff/')
