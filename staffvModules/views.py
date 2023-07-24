
from django.db import connection
from django.shortcuts import get_object_or_404,render, redirect
from django.http import JsonResponse
from .models import Course,Project,AdminRole,SchoolRole,UniRole
from user.models import Log,User,Permission
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import TeachCourse, TeachProject, TeachAdminRole, TeachSchoolRoles, TeachUniRoles
import json
from staff.models import Staff
from django.db.models import Sum
from django.db.models import Q


# Create your views here.

def check_login_decorator(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if 'username' not in request.session and request.user_agent.is_mobile:
            return redirect('/user/wap/login')
        
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
            # Find the permission with the specified permission_id and menu_id=1
            permission = Permission.objects.get(permission=user_permission_name, menu_id=1)
            if permission.position_id == 0:
                return redirect('/setting/warn')
        return view_func(request, *args, **kwargs)
    return _wrapped_view



@check_login_decorator
def list(request):
    if request.user_agent.is_mobile:
        if 'username' in request.session:
            staff_list = Staff.objects.filter(is_delete=0)
            context = {'staffList': staff_list}
            return render(request, 'staff_h5.html', context)
        return render(request, 'wap_login.html', context)     
    else:    
        # Retrieve all non-deleted courses from the database
        courses = Course.objects.filter(is_delete=0)

        # Search functionality
        hsQuery = request.GET.get('hsQuery')
        typeQuery = request.GET.get('typeQuery')
        codeQuery = request.GET.get('codeQuery')

        if hsQuery or typeQuery or codeQuery:
            # Filter courses based on the search query and is_delete condition
            courses = courses.filter(
                Q(hs__icontains=hsQuery) | 
                Q(type__icontains=typeQuery) | 
                Q(code__icontains=codeQuery)
            )

        # Pagination
        paginator = Paginator(courses, 10)  # Show 10 courses per page
        page_number = request.GET.get('page')
        courses = paginator.get_page(page_number)

        # Pass the courses, search queries, and pagination to the template
        context = {'courses': courses, 'hsQuery': hsQuery, 'typeQuery': typeQuery, 'codeQuery': codeQuery}
        return render(request, 'list.html', context)
 
@check_login_decorator
def full_list(request, category=None):
    # Retrieve all non-deleted items from the database based on the category
    if category == 'project':
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT initials FROM balancer_staff WHERE id IN (
                    SELECT a.staff_id FROM balancer_teach_project AS a 
                    LEFT JOIN balancer_project AS b ON b.code = a.project_name 
                    WHERE b.is_delete = 0
                )
            """)
            rows = cursor.fetchall()
            staff_list = [item[0] for item in rows]  # Assuming 'initials' is the first column in your result set

        items = Project.objects.filter(is_delete=0)
        for item in items:
            code = item.code
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT f.share FROM (
                        SELECT id AS staff_id FROM balancer_staff WHERE id IN (
                            SELECT a.staff_id FROM balancer_teach_project AS a 
                            LEFT JOIN balancer_project AS b ON b.code = a.project_name 
                            WHERE b.is_delete = 0
                        )
                    ) as c 
                    LEFT JOIN (
                        SELECT d.staff_id, d.share FROM balancer_teach_project AS d 
                        LEFT JOIN balancer_project AS e ON e.code = d.project_name 
                        WHERE e.is_delete = 0 AND e.code = %s 
                        GROUP BY d.staff_id
                    ) as f 
                    ON c.staff_id = f.staff_id
                """, [code])
                result = cursor.fetchall()

                # Attach the result to the item
                item.share = result
        template_name = 'full/full_project_list.html'
        context = {'list': items, 'staff_list': staff_list}
        return render(request, template_name, context)
    elif category == 'adminrole':
       with connection.cursor() as cursor:
            cursor.execute("""
                SELECT initials FROM balancer_staff WHERE id IN (
                    SELECT a.staff_id FROM balancer_teach_admin_role AS a 
                    LEFT JOIN balancer_admin_role AS b ON b.name = a.role_name
                    WHERE b.is_delete = 0
                )
            """)
            rows = cursor.fetchall()
            staff_list = [item[0] for item in rows]  # Assuming 'initials' is the first column in your result set

       items = AdminRole.objects.filter(is_delete=0)
       for item in items:
            name = item.name
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT f.share FROM (
                        SELECT id AS staff_id FROM balancer_staff WHERE id IN (
                            SELECT a.staff_id FROM balancer_teach_admin_role AS a 
                            LEFT JOIN balancer_admin_role AS b ON b.name = a.role_name 
                            WHERE b.is_delete = 0
                        )
                    ) as c 
                    LEFT JOIN (
                        SELECT d.staff_id, d.share FROM balancer_teach_admin_role AS d 
                        LEFT JOIN balancer_admin_role AS e ON e.name = d.role_name 
                        WHERE e.is_delete = 0 AND e.name = %s 
                        GROUP BY d.staff_id
                    ) as f 
                    ON c.staff_id = f.staff_id
                """, [name])
                result = cursor.fetchall()

                # Attach the result to the item
                item.share = result
       template_name = 'full/full_adminrole_list.html'
       context = {'list': items, 'staff_list': staff_list}
       return render(request, template_name, context)
    elif category == 'schoolrole':
       with connection.cursor() as cursor:
            cursor.execute("""
                SELECT initials FROM balancer_staff WHERE id IN (
                    SELECT a.staff_id FROM balancer_teach_school_role AS a 
                    LEFT JOIN balancer_school_role AS b ON b.name = a.role_name
                    WHERE b.is_delete = 0
                )
            """)
            rows = cursor.fetchall()
            staff_list = [item[0] for item in rows]  # Assuming 'initials' is the first column in your result set

       items = SchoolRole.objects.filter(is_delete=0)
       for item in items:
            name = item.name
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT f.share FROM (
                        SELECT id AS staff_id FROM balancer_staff WHERE id IN (
                            SELECT a.staff_id FROM balancer_teach_school_role AS a 
                            LEFT JOIN balancer_school_role AS b ON b.name = a.role_name 
                            WHERE b.is_delete = 0
                        )
                    ) as c 
                    LEFT JOIN (
                        SELECT d.staff_id, d.share FROM balancer_teach_school_role AS d 
                        LEFT JOIN balancer_school_role AS e ON e.name = d.role_name 
                        WHERE e.is_delete = 0 AND e.name = %s 
                        GROUP BY d.staff_id
                    ) as f 
                    ON c.staff_id = f.staff_id
                """, [name])
                result = cursor.fetchall()

                # Attach the result to the item
                item.share = result
       template_name = 'full/full_schoolrole_list.html'
       context = {'list': items, 'staff_list': staff_list}
       return render(request, template_name, context)
    elif category == 'unirole':
       with connection.cursor() as cursor:
            cursor.execute("""
                SELECT initials FROM balancer_staff WHERE id IN (
                    SELECT a.staff_id FROM balancer_teach_school_role AS a 
                    LEFT JOIN balancer_school_role AS b ON b.name = a.role_name
                    WHERE b.is_delete = 0
                )
            """)
            rows = cursor.fetchall()
            staff_list = [item[0] for item in rows]  # Assuming 'initials' is the first column in your result set

       items = SchoolRole.objects.filter(is_delete=0)
       for item in items:
            name = item.name
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT f.share FROM (
                        SELECT id AS staff_id FROM balancer_staff WHERE id IN (
                            SELECT a.staff_id FROM balancer_teach_uni_role AS a 
                            LEFT JOIN balancer_uni_role AS b ON b.name = a.role_name 
                            WHERE b.is_delete = 0
                        )
                    ) as c 
                    LEFT JOIN (
                        SELECT d.staff_id, d.share FROM balancer_teach_uni_role AS d 
                        LEFT JOIN balancer_uni_role AS e ON e.name = d.role_name 
                        WHERE e.is_delete = 0 AND e.name = %s 
                        GROUP BY d.staff_id
                    ) as f 
                    ON c.staff_id = f.staff_id
                """, [name])
                result = cursor.fetchall()

                # Attach the result to the item
                item.share = result
       template_name = 'full/full_unirole_list.html'
       context = {'list': items, 'staff_list': staff_list}
       return render(request, template_name, context)
    else:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT initials FROM balancer_staff WHERE id IN (
                    SELECT a.staff_id FROM balancer_teach_course AS a 
                    LEFT JOIN balancer_course AS b ON b.code = a.course_name 
                    WHERE b.is_delete = 0
                )
            """)
            rows = cursor.fetchall()
            staff_list = [item[0] for item in rows]  # Assuming 'initials' is the first column in your result set

        items = Course.objects.filter(is_delete=0)
        for item in items:
            code = item.code
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT f.share FROM (
                        SELECT id AS staff_id FROM balancer_staff WHERE id IN (
                            SELECT a.staff_id FROM balancer_teach_course AS a 
                            LEFT JOIN balancer_course AS b ON b.code = a.course_name 
                            WHERE b.is_delete = 0
                        )
                    ) as c 
                    LEFT JOIN (
                        SELECT d.staff_id, d.share FROM balancer_teach_course AS d 
                        LEFT JOIN balancer_course AS e ON e.code = d.course_name 
                        WHERE e.is_delete = 0 AND e.code = %s 
                        GROUP BY d.staff_id
                    ) as f 
                    ON c.staff_id = f.staff_id
                """, [code])
                result = cursor.fetchall()

                # Attach the result to the item
                item.share = result


        template_name = 'full/full_course_list.html'
        context = {'list': items, 'staff_list': staff_list}
        return render(request, template_name, context)
    
    context = {'list': items}
    return render(request, template_name, context)


@check_login_decorator
def project_list(request):
    # Retrieve all non-deleted courses from the database
    projects = Project.objects.filter(is_delete=0)

     # Search functionality
    project_query = request.GET.get('query')
    if project_query:
        # Filter courses based on the search query and is_delete condition
        projects = projects.filter(code__icontains=project_query)    

    # Pagination
    paginator = Paginator(projects.order_by('id'), 10)  # Show 10 courses per page
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    # Pass the courses and search query to the template
    context = {'projects': projects, 'query': project_query}
    return render(request, 'project_list.html', context)

@check_login_decorator
def adminrole_list(request):
    # Retrieve all non-deleted courses from the database
    adminroles = AdminRole.objects.filter(is_delete=0)

     # Search functionality
    adminrole_query = request.GET.get('query')
    if adminrole_query:
        # Filter courses based on the search query and is_delete condition
        adminroles = adminroles.filter(name__icontains=adminrole_query)    

    # Pagination
    paginator = Paginator(adminroles.order_by('id'), 10)  # Show 10 courses per page
    page_number = request.GET.get('page')
    adminroles = paginator.get_page(page_number)

    # Pass the courses and search query to the template
    context = {'adminroles': adminroles, 'query': adminrole_query}
    return render(request, 'adminrole_list.html', context)

@check_login_decorator
def schoolrole_list(request):
    # Retrieve all non-deleted courses from the database
    schoolroles = SchoolRole.objects.filter(is_delete=0)

     # Search functionality
    schoolrole_query = request.GET.get('query')
    if schoolrole_query:
        # Filter courses based on the search query and is_delete condition
        schoolroles = schoolroles.filter(name__icontains=schoolrole_query)    

    # Pagination
    paginator = Paginator(schoolroles.order_by('id'), 10)  # Show 10 courses per page
    page_number = request.GET.get('page')
    schoolroles = paginator.get_page(page_number)

    # Pass the courses and search query to the template
    context = {'schoolroles': schoolroles, 'query': schoolrole_query}
    return render(request, 'schoolrole_list.html', context)

@check_login_decorator
def unirole_list(request):
    # Retrieve all non-deleted courses from the database
    uniroles = UniRole.objects.filter(is_delete=0)

     # Search functionality
    unirole_query = request.GET.get('query')
    if unirole_query:
        # Filter courses based on the search query and is_delete condition
        uniroles = uniroles.filter(name__icontains=unirole_query)    

    # Pagination
    paginator = Paginator(uniroles.order_by('id'), 10)  # Show 10 courses per page
    page_number = request.GET.get('page')
    uniroles = paginator.get_page(page_number)

    # Pass the courses and search query to the template
    context = {'uniroles': uniroles, 'query': unirole_query}
    return render(request, 'unirole_list.html', context)

@check_login_decorator
def detail(request, staffId):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')  # 获取请求体中的JSON字符串
        data = json.loads(json_str)  # 将JSON字符串解析为Python对象

        course_data = data['course']
        project_data = data['project']
        admin_role_data = data['adminrole']
        school_role_data = data['school']
        uni_role_data = data['uni']

        # 清空对应staff_id的数据
        TeachCourse.objects.filter(staff_id=staffId).delete()
        TeachProject.objects.filter(staff_id=staffId).delete()
        TeachAdminRole.objects.filter(staff_id=staffId).delete()
        TeachSchoolRoles.objects.filter(staff_id=staffId).delete()
        TeachUniRoles.objects.filter(staff_id=staffId).delete()

        # 插入新的数据
        for course in course_data:
            TeachCourse.objects.create(
                staff_id=staffId,
                course_name=course['courseName'],
                credits=course['credits'],
                alpha=course['alpha'],
                beta=course['beta'],
                num_students=course['numStudents'],
                delta=course['delta'],
                share=course['share'],
                coordinator=course['coordinator'],
                total_hours = int(course['credits']) * (float(course['alpha']) * float(course['delta']) + float(course['beta']) * int(course['numStudents'])) * float(course['share']) + float(course['coordinator'])
            )

        for project in project_data:
            TeachProject.objects.create(
                staff_id=staffId,
                project_name=project['projectName'],
                credits=project['credits'],
                alpha=project['alpha'],
                beta=project['beta'],
                num_students=project['numGroupsStudents'],
                delta=project['delta'],
                share=project['share'],
                coordinator=project['coordinator'],
                total_hours = int(project['credits']) * (float(project['alpha']) * float(project['delta']) + float(project['beta']) * int(project['numGroupsStudents'])) * float(project['share']) + float(project['coordinator'])
            )

        for admin_role in admin_role_data:
            TeachAdminRole.objects.create(
                staff_id=staffId,
                role_name=admin_role['role'],
                credits=admin_role['credits'],
                alpha=admin_role['alpha'],
                beta=admin_role['beta'],
                num_students=admin_role['numGroupsStudents'],
                delta=admin_role['delta'],
                share=admin_role['share'],
                coordinator=admin_role['coordinator'],
                total_hours = float(admin_role['credits']) * (float(admin_role['alpha']) * float(admin_role['delta']) + float(admin_role['beta']) * int(admin_role['numGroupsStudents'])) * float(admin_role['share']) + float(admin_role['coordinator'])
            )

        for school_role in school_role_data:
            TeachSchoolRoles.objects.create(
                staff_id=staffId,
                role_name=school_role['role'],
                credits=school_role['credits'],
                alpha=school_role['alpha'],
                beta=school_role['beta'],
                num_students=school_role['numGroupsStudents'],
                delta=school_role['delta'],
                share=school_role['share'],
                total_hours = float(school_role['credits']) * (float(school_role['alpha']) * float(school_role['delta']) + float(school_role['beta']) * int(school_role['numGroupsStudents'])) * float(school_role['share']) + float(school_role['coordinator'])
            )

        for uni_role in uni_role_data:
            TeachUniRoles.objects.create(
                staff_id=staffId,
                role_name=uni_role['role'],
                credits=uni_role['credits'],
                alpha=uni_role['alpha'],
                beta=uni_role['beta'],
                num_students=uni_role['numGroupsStudents'],
                delta=uni_role['delta'],
                share=uni_role['share'],
                coordinator=uni_role['coordinator'],
                total_hours = float(uni_role['credits']) * (float(uni_role['alpha']) * float(uni_role['delta']) + float(uni_role['beta']) * int(uni_role['numGroupsStudents'])) * float(uni_role['share']) + float(uni_role['coordinator'])
            )

        user_id = request.session.get('user_id')
        operation_details = "staffvMoudles detail save"
                
        if user_id:
            Log.create_log(user_id, operation_details)

        print("Data saved successfully.")  # 打印保存成功的提示

    # 从数据库中获取数据
    #select * from balancer_teach_course as a left join balancer_course as b on a.course_name = b.code where b.is_delete = 0
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
    courses_shares = sum([float(e.share) for e in courses])
    projects_hours = sum([float(p.total_hours) for p in projects])
    admin_roles_hours = sum([float(a.total_hours) for a in admin_roles])
    school_roles_hours = sum([float(s.total_hours) for s in school_roles])
    uni_roles_hours = sum([float(u.total_hours) for u in uni_roles])

    staff_total_hours = courses_hours + projects_hours + admin_roles_hours +  school_roles_hours + uni_roles_hours
    staff_total_no_project_hours = courses_hours  + admin_roles_hours +  school_roles_hours + uni_roles_hours
    staff_permitt_hours = Staff.objects.get(id=staffId).adjusted_max
    staff_first_name = Staff.objects.get(id=staffId).first_name
    staff_last_name = Staff.objects.get(id=staffId).last_name
    staff_name = staff_first_name + " " + staff_last_name
    # For HS1
    courses_hs1 = TeachCourse.objects.raw("""
        SELECT * 
        FROM balancer_teach_course AS a 
        LEFT JOIN balancer_course AS b 
        ON a.course_name = b.code 
        WHERE b.is_delete = 0 and a.staff_id = %s and b.hs = 'HS1'
    """, [staffId])
    courses_hs1_hours = sum([float(c.total_hours) for c in courses_hs1])
    courses_hs1_shares = sum([float(e.share) for e in courses_hs1])

    # For HS2
    courses_hs2 = TeachCourse.objects.raw("""
        SELECT * 
        FROM balancer_teach_course AS a 
        LEFT JOIN balancer_course AS b 
        ON a.course_name = b.code 
        WHERE b.is_delete = 0 and a.staff_id = %s and b.hs = 'HS2'
    """, [staffId])
    courses_hs2_hours = sum([float(c.total_hours) for c in courses_hs2])
    courses_hs2_shares = sum([float(e.share) for e in courses_hs2])

    # For HS3
    courses_hs3 = TeachCourse.objects.raw("""
        SELECT * 
        FROM balancer_teach_course AS a 
        LEFT JOIN balancer_course AS b 
        ON a.course_name = b.code 
        WHERE b.is_delete = 0 and a.staff_id = %s and b.hs = 'HS3'
    """, [staffId])
    courses_hs3_hours = sum([float(c.total_hours) for c in courses_hs3])
    courses_hs3_shares = sum([float(e.share) for e in courses_hs3])

    context = {
        'courses': courses,
        'projects': projects,
        'admin_roles': admin_roles,
        'school_roles': school_roles,
        'uni_roles': uni_roles,
        'courses_hours': courses_hours,
        'projects_hours': projects_hours,
        'admin_roles_hours': admin_roles_hours,
        'school_roles_hours': school_roles_hours,
        'uni_roles_hours': uni_roles_hours,
        'courses_shares': courses_shares,
        'staff_total_hours': staff_total_hours,
        'staff_total_no_project_hours': staff_total_no_project_hours,
        'staff_permitt_hours': staff_permitt_hours,
        'staff_total_hours_left': float(staff_permitt_hours) - staff_total_hours,
        'courses_hs1_hours': courses_hs1_hours,
        'courses_hs1_shares': courses_hs1_shares,
        'courses_hs2_hours': courses_hs2_hours,
        'courses_hs2_shares': courses_hs2_shares,
        'courses_hs3_hours': courses_hs3_hours,
        'courses_hs3_shares': courses_hs3_shares,
        "staff_name":staff_name
    }

    return render(request, 'detail.html', context)

@check_login_decorator
def staffvModules_course_edit(request, courseId):
    # Retrieve the course object based on the courseId
    course = Course.objects.get(id=courseId)

    if request.method == 'POST':
        # Retrieve the form data from the request
        code = request.POST.get('code')
        linked_courses = request.POST.get('linked_courses')
        unlinked_relatives = request.POST.get('unlinked_relatives')
        name = request.POST.get('name')
        est_num_students = request.POST.get('est_num_students')
        hours = request.POST.get('hours')
        if hours == '':
           hours = 0
        course_type = request.POST.get('type')  # 获取type字段的值
        hs = request.POST.get('hs')

        # Update the course object with the form data
        course.code = code
        course.linked_courses = linked_courses
        course.unlinked_relatives = unlinked_relatives
        course.name = name
        course.est_num_students = est_num_students
        course.hours = hours
        course.type = course_type  # 设置type字段的值
        course.hs = hs

        # Save the updated course object to the database
        course.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_course_edit"
                
        if user_id:
            Log.create_log(user_id, operation_details)

        # Redirect to the staffvModules list page
        return redirect('/staffvModules/')

    # Pass the course object to the template
    context = {'course': course}
    return render(request, 'staffvModules_course_edit.html', context)

@check_login_decorator
def staffvModules_course_add(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        linked_courses = request.POST.get('linked_courses')
        unlinked_relatives = request.POST.get('unlinked_relatives')
        name = request.POST.get('name')
        est_num_students = request.POST.get('est_num_students')
        hours = request.POST.get('hours')
        if hours == '':
           hours = 0
        course_type = request.POST.get('type') 
        if course_type == '':
           course_type = "Standard classroom based"
        hs = request.POST.get('hs')
           
        course = Course.objects.create(
            code=code,
            linked_courses=linked_courses,
            unlinked_relatives=unlinked_relatives,
            name=name,
            type=course_type,
            num_staff_allocated=0,
            est_num_students=est_num_students,
            hours=hours,
            hs = hs
        )

        course.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_course_add"
                
        if user_id:
            Log.create_log(user_id, operation_details)

        return redirect('/staffvModules/')

    return render(request, 'staffvModules_course_add.html')

@check_login_decorator
def staffvModules_course_del(request, courseId):
    course = get_object_or_404(Course, id=courseId)
    course.is_delete = 1
    course.save()
    user_id = request.session.get('user_id')
    operation_details = "staffvModules_course_del"
                
    if user_id:
        Log.create_log(user_id, operation_details)

    return redirect('/staffvModules/')

@check_login_decorator
def staffvModules_project_edit(request, projectId):
    # Retrieve the project object based on the projectId
    project = Project.objects.get(id=projectId)

    if request.method == 'POST':
        # Retrieve the form data from the request
        code = request.POST.get('code')
        linked_courses = request.POST.get('linked_courses')
        unlinked_relatives = request.POST.get('unlinked_relatives')
        name = request.POST.get('name')
        est_num_students = request.POST.get('est_num_students')
        hours = request.POST.get('hours')
        if hours == '':
           hours = 0
        project_type = request.POST.get('type')  # 获取type字段的值

        # Update the project object with the form data
        project.code = code
        project.linked_courses = linked_courses
        project.unlinked_relatives = unlinked_relatives
        project.name = name
        project.est_num_students = est_num_students
        project.hours = hours
        project.type = project_type  # 设置type字段的值

        # Save the updated project object to the database
        project.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_project_edit"
                    
        if user_id:
            Log.create_log(user_id, operation_details)
        # Redirect to the staffvModules project list page
        return redirect('/staffvModules/project/')

    # Pass the project object to the template
    context = {'project': project}
    return render(request, 'staffvModules_project_edit.html', context)

@check_login_decorator
def staffvModules_project_add(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        linked_courses = request.POST.get('linked_courses')
        unlinked_relatives = request.POST.get('unlinked_relatives')
        name = request.POST.get('name')
        est_num_students = request.POST.get('est_num_students')
        hours = request.POST.get('hours')
        if hours == '':
           hours = 0
        project_type = request.POST.get('type')  # 获取type字段的值

        project = Project.objects.create(
            code=code,
            linked_courses=linked_courses,
            unlinked_relatives=unlinked_relatives,
            name=name,
            num_staff_allocated=0,
            est_num_students=est_num_students,
            hours=hours,
            type=project_type  # 设置type字段的值
        )

        project.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_project_add"
                    
        if user_id:
            Log.create_log(user_id, operation_details)

        return redirect('/staffvModules/project/')

    return render(request, 'staffvModules_project_add.html')

@check_login_decorator
def staffvModules_project_del(request, projectId):
    project = get_object_or_404(Project, id=projectId)
    project.is_delete = 1
    project.save()
    user_id = request.session.get('user_id')
    operation_details = "staffvModules_project_del"
                    
    if user_id:
        Log.create_log(user_id, operation_details)

    return redirect('/staffvModules/project/')


@check_login_decorator
def staffvModules_adminrole_edit(request, adminroleId):
    # Retrieve the course object based on the courseId
    adminrole = AdminRole.objects.get(id=adminroleId)

    if request.method == 'POST':
        # Retrieve the form data from the request
        name = request.POST.get('name')
        hours = request.POST.get('hours')
        crit =  request.POST.get('crit')
        if hours == '':
           hours = 0

        # Update the course object with the form data
        adminrole.crit = crit
        adminrole.name = name
        adminrole.hours = hours

        # Save the updated course object to the database
        adminrole.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_adminrole_edit"
                        
        if user_id:
            Log.create_log(user_id, operation_details)
        # Redirect to the staffvModules list page
        return redirect('/staffvModules/adminRole/')

    # Pass the course object to the template
    context = {'adminrole': adminrole}
    return render(request, 'staffvModules_adminrole_edit.html', context)

@check_login_decorator
def staffvModules_adminrole_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hours = request.POST.get('hours')
        crit =  request.POST.get('crit')
        if hours == '':
           hours = 0

        adminrole = AdminRole.objects.create(
            name=name,
            num_staff_allocated=0,
            hours=hours,
            crit=crit
        )

        adminrole.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_adminrole_add"
                        
        if user_id:
            Log.create_log(user_id, operation_details)

        return redirect('/staffvModules/adminRole/')

    return render(request, 'staffvModules_adminrole_add.html')

@check_login_decorator
def staffvModules_adminrole_del(request, adminroleId):
    adminrole = get_object_or_404(AdminRole, id=adminroleId)
    adminrole.is_delete = 1
    adminrole.save()
    user_id = request.session.get('user_id')
    operation_details = "staffvModules_adminrole_del"
                        
    if user_id:
        Log.create_log(user_id, operation_details)

    return redirect('/staffvModules/adminRole/')

@check_login_decorator
def staffvModules_schoolrole_edit(request, schoolroleId):
    # Retrieve the course object based on the courseId
    schoolrole = SchoolRole.objects.get(id=schoolroleId)

    if request.method == 'POST':
        # Retrieve the form data from the request
        name = request.POST.get('name')
        hours = request.POST.get('hours')
        crit =  request.POST.get('crit')
        if hours == '':
           hours = 0

        # Update the course object with the form data
        schoolrole.crit = crit
        schoolrole.name = name
        schoolrole.hours = hours

        # Save the updated course object to the database
        schoolrole.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_schoolrole_edit"
                            
        if user_id:
            Log.create_log(user_id, operation_details)

        # Redirect to the staffvModules list page
        return redirect('/staffvModules/schoolRole/')

    # Pass the course object to the template
    context = {'schoolrole': schoolrole}
    return render(request, 'staffvModules_schoolrole_edit.html', context)

@check_login_decorator
def staffvModules_schoolrole_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hours = request.POST.get('hours')
        crit =  request.POST.get('crit')
        if hours == '':
           hours = 0

        schoolrole = SchoolRole.objects.create(
            name=name,
            num_staff_allocated=0,
            hours=hours,
            crit=crit
        )

        schoolrole.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_schoolrole_add"
                            
        if user_id:
            Log.create_log(user_id, operation_details)

        return redirect('/staffvModules/schoolRole/')

    return render(request, 'staffvModules_schoolrole_add.html')

@check_login_decorator
def staffvModules_schoolrole_del(request, schoolroleId):
    schoolrole = get_object_or_404(SchoolRole, id=schoolroleId)
    schoolrole.is_delete = 1
    schoolrole.save()
    user_id = request.session.get('user_id')
    operation_details = "staffvModules_schoolrole_del"
                            
    if user_id:
        Log.create_log(user_id, operation_details)

    return redirect('/staffvModules/schoolRole/')


@check_login_decorator
def staffvModules_unirole_edit(request, uniroleId):
    # Retrieve the course object based on the courseId
    unirole = UniRole.objects.get(id=uniroleId)

    if request.method == 'POST':
        # Retrieve the form data from the request
        name = request.POST.get('name')
        hours = request.POST.get('hours')
        crit =  request.POST.get('crit')
        if hours == '':
           hours = 0

        # Update the course object with the form data
        unirole.crit = crit
        unirole.name = name
        unirole.hours = hours

        # Save the updated course object to the database
        unirole.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_unirole_edit"
                                
        if user_id:
            Log.create_log(user_id, operation_details)

        # Redirect to the staffvModules list page
        return redirect('/staffvModules/uniRole/')

    # Pass the course object to the template
    context = {'unirole': unirole}
    return render(request, 'staffvModules_unirole_edit.html', context)

@check_login_decorator
def staffvModules_unirole_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hours = request.POST.get('hours')
        crit =  request.POST.get('crit')
        if hours == '':
           hours = 0

        unirole = UniRole.objects.create(
            name=name,
            num_staff_allocated=0,
            hours=hours,
            crit=crit
        )

        unirole.save()
        user_id = request.session.get('user_id')
        operation_details = "staffvModules_unirole_add"
                                
        if user_id:
            Log.create_log(user_id, operation_details)

        return redirect('/staffvModules/uniRole/')

    return render(request, 'staffvModules_unirole_add.html')

@check_login_decorator
def staffvModules_unirole_del(request, uniroleId):
    unirole = get_object_or_404(UniRole, id=uniroleId)
    unirole.is_delete = 1
    unirole.save()
    user_id = request.session.get('user_id')
    operation_details = "staffvModules_unirole_del"
                                
    if user_id:
        Log.create_log(user_id, operation_details)

    return redirect('/staffvModules/uniRole/')

@check_login_decorator
def staff_list(request, name, type="course"):
    staff_list = []
    
    if type == "course":
        # Retrieve the TeachCourse objects based on the provided name and type
        teach_courses = TeachCourse.objects.filter(course_name=name)
        
        # Iterate over the retrieved TeachCourse objects
        for teach_course in teach_courses:
            # Retrieve the staff information using the staff_id from the TeachCourse object
            staff = Staff.objects.get(id=teach_course.staff_id)
            
            # Create a dictionary containing the staff information and share value
            staff_info = {
                'staff_id': staff.id,
                'name': staff.initials,
                'share': teach_course.share
            }
            
            # Append the staff information dictionary to the staff_list
            staff_list.append(staff_info)
    
    elif type == "project":
       # Retrieve the TeachCourse objects based on the provided name and type
        teach_projects = TeachProject.objects.filter(project_name=name)
        
        # Iterate over the retrieved TeachCourse objects
        for teach_project in teach_projects:
            # Retrieve the staff information using the staff_id from the TeachCourse object
            staff = Staff.objects.get(id=teach_project.staff_id)
            
            # Create a dictionary containing the staff information and share value
            staff_info = {
                'staff_id': staff.id,
                'name': staff.initials,
                'share': teach_project.share
            }
            
            # Append the staff information dictionary to the staff_list
            staff_list.append(staff_info)
    elif type == "adminrole":
       # Retrieve the TeachCourse objects based on the provided name and type
        teach_adminroles = TeachAdminRole.objects.filter(role_name=name)
        
        # Iterate over the retrieved TeachCourse objects
        for teach_adminrole in teach_adminroles:
            # Retrieve the staff information using the staff_id from the TeachCourse object
            staff = Staff.objects.get(id=teach_adminrole.staff_id)
            
            # Create a dictionary containing the staff information and share value
            staff_info = {
                'staff_id': staff.id,
                'name': staff.initials,
                'share': teach_adminrole.share
            }
            
            # Append the staff information dictionary to the staff_list
            staff_list.append(staff_info)
    elif type == "schoolrole":
       # Retrieve the TeachCourse objects based on the provided name and type
        teach_schoolroles = TeachSchoolRoles.objects.filter(role_name=name)
        
        # Iterate over the retrieved TeachCourse objects
        for teach_schoolrole in teach_schoolroles:
            # Retrieve the staff information using the staff_id from the TeachCourse object
            staff = Staff.objects.get(id=teach_schoolrole.staff_id)
            
            # Create a dictionary containing the staff information and share value
            staff_info = {
                'staff_id': staff.id,
                'name': staff.initials,
                'share': teach_schoolrole.share
            }
            
            # Append the staff information dictionary to the staff_list
            staff_list.append(staff_info)
    else:
       # Retrieve the TeachCourse objects based on the provided name and type
        teach_uniroles = TeachUniRoles.objects.filter(role_name=name)
        
        # Iterate over the retrieved TeachCourse objects
        for teach_unirole in teach_uniroles:
            # Retrieve the staff information using the staff_id from the TeachCourse object
            staff = Staff.objects.get(id=teach_unirole.staff_id)
            
            # Create a dictionary containing the staff information and share value
            staff_info = {
                'staff_id': staff.id,
                'name': staff.initials,
                'share': teach_unirole.share
            }
            
            # Append the staff information dictionary to the staff_list
            staff_list.append(staff_info)                       
    
    # Create a JSON response with the staff_list
    response_data = {
        'staff_list': staff_list
    }
    
    # Return the JSON response
    return JsonResponse(response_data)

@check_login_decorator
def hs_total_list(request):
    page = request.GET.get('page', 1)

    staffs = Staff.objects.all()

    for staff in staffs:
        hs1_courses = Course.objects.filter(hs='HS1').values_list('code', flat=True)
        hs2_courses = Course.objects.filter(hs='HS2').values_list('code', flat=True)
        hs3_courses = Course.objects.filter(hs='HS3').values_list('code', flat=True)

        staff.hs1_share = TeachCourse.objects.filter(staff_id=staff.id, course_name__in=hs1_courses).aggregate(Sum('share'))['share__sum'] or 0
        staff.hs2_share = TeachCourse.objects.filter(staff_id=staff.id, course_name__in=hs2_courses).aggregate(Sum('share'))['share__sum'] or 0
        staff.hs3_share = TeachCourse.objects.filter(staff_id=staff.id, course_name__in=hs3_courses).aggregate(Sum('share'))['share__sum'] or 0
        staff.hs_total_share = staff.hs1_share + staff.hs2_share + staff.hs3_share
        
    paginator = Paginator(staffs, 10)

    try:
        staffs = paginator.page(page)
    except PageNotAnInteger:
        staffs = paginator.page(1)
    except EmptyPage:
        staffs = paginator.page(paginator.num_pages)

    return render(request, 'hs_list.html', {'staffs': staffs})

@check_login_decorator
def full_edit(request, type):
    if request.method == "POST":
        data = json.loads(request.body)

        if type == 'course':
            for row in data:
                try:
                    course = Course.objects.get(id=row[0])  # 通过code查询
                    # 更新字段
                    course.code = row[1]
                    course.hs = row[2]
                    course.type = row[3]
                    course.linked_courses = row[4]
                    course.unlinked_relatives = row[5]
                    course.name = row[6]
                    course.num_staff_allocated = row[7]
                    course.est_num_students = row[8]
                    course.hours = row[9]
                    course.save()  # 更新数据库

                except ObjectDoesNotExist:
                    print(f'Course with code {row[0]} does not exist')

        elif type == 'project':
            for row in data:
                try:
                    project = Project.objects.get(id=row[0])  # 通过code查询
                    # 更新字段
                    project.code = row[1]
                    project.type = row[2]
                    project.linked_courses = row[3]
                    project.unlinked_relatives = row[4]
                    project.name = row[5]
                    project.num_staff_allocated = row[6]
                    project.est_num_students = row[7]
                    project.hours = row[8]
                    project.save()  # 更新数据库

                except ObjectDoesNotExist:
                    print(f'Project with code {row[0]} does not exist')

        elif type == 'adminrole':
            for row in data:
                try:
                    adminrole = AdminRole.objects.get(id=row[0])  # 通过code查询
                    # 更新字段
                    adminrole.name = row[1]
                    adminrole.hours = row[2]
                    adminrole.crit = row[3]
                    adminrole.num_staff_allocated = row[4]
                    adminrole.save()  # 更新数据库

                except ObjectDoesNotExist:
                    print(f'adminrole with code {row[0]} does not exist')


        elif type == 'schoolrole':
           for row in data:
                try:
                    schoolrole = SchoolRole.objects.get(id=row[0])  # 通过code查询
                    # 更新字段
                    schoolrole.name = row[1]
                    schoolrole.hours = row[2]
                    schoolrole.crit = row[3]
                    schoolrole.num_staff_allocated = row[4]
                    schoolrole.save()  # 更新数据库

                except ObjectDoesNotExist:
                    print(f'schoolrole with code {row[0]} does not exist')

        elif type == 'unirole':
           for row in data:
                try:
                    unirole = UniRole.objects.get(id=row[0])  # 通过code查询
                    # 更新字段
                    unirole.name = row[1]
                    unirole.hours = row[2]
                    unirole.crit = row[3]
                    unirole.num_staff_allocated = row[4]
                    unirole.save()  # 更新数据库

                except ObjectDoesNotExist:
                    print(f'unirole with code {row[0]} does not exist')
           
        else:
            return JsonResponse({'status':'failed', 'message': 'Invalid type parameter'}, status=400)
         
        user_id = request.session.get('user_id')
        operation_details = "full_screen_edit"
                                    
        if user_id:
            Log.create_log(user_id, operation_details)

        # 返回一个成功的响应
        return JsonResponse({'status':'success', 'message': 'Data updated successfully'}, status=200)

    # 如果不是 POST 请求，返回一个错误响应
    return JsonResponse({'status':'failed', 'message': 'Not a POST request'}, status=400)

