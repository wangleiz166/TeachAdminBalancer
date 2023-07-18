from django.shortcuts import render
from staffvModules.models import TeachCourse,TeachProject,TeachAdminRole,TeachSchoolRoles,TeachUniRoles,Course,Project,AdminRole,SchoolRole,UniRole
from django.db import connection
from django.db.models import Sum

from staffvModules.views import project_list
    

# Create your views here.

def total_work_list(request):
    with connection.cursor() as cursor:
        sql_query = """
            SELECT c.code, tc.credits, tc.alpha, tc.beta, tc.num_students, tc.delta, tc.coordinator, tc.total_hours
            FROM balancer_course AS c
            INNER JOIN balancer_teach_course AS tc ON c.code = tc.course_name
        """
        cursor.execute(sql_query)
        results = cursor.fetchall()

    course_data = []
    for row in results:
        code = row[0]
        credits = row[1]
        alpha = row[2]
        beta = row[3]
        num_students = row[4]
        delta = row[5]
        coordinator = row[6]
        total_hours = row[7]

        course = {
            'code': code,
            'credits': credits,
            'alpha': alpha,
            'beta': beta,
            'num_students': num_students,
            'delta': delta,
            'coordinator': coordinator,
            'total_hours': total_hours,
        }

        course_data.append(course)

    with connection.cursor() as cursor:
        sql_query = """
            SELECT p.code, tp.credits, tp.alpha, tp.beta, tp.num_students, tp.delta, tp.coordinator, tp.total_hours
            FROM balancer_project AS p
            INNER JOIN balancer_teach_project AS tp ON p.code = tp.project_name
        """
        cursor.execute(sql_query)
        results = cursor.fetchall()
    project_data=[]
    for row in results:
        code = row[0]
        credits = row[1]
        alpha = row[2]
        beta = row[3]
        num_students = row[4]
        delta = row[5]
        coordinator = row[6]
        total_hours = row[7]

        project= {
            'code': code,
            'credits': credits,
            'alpha': alpha,
            'beta': beta,
            'num_students': num_students,
            'delta': delta,
            'coordinator': coordinator,
            'total_hours': total_hours,
            }
        project_data.append(project)

    course_total_hours = sum(float(course['total_hours']) for course in course_data)
    project_total_hours = sum(float(project['total_hours']) for project in project_data)
    total_hours_sum = course_total_hours + project_total_hours

    context = {
        'courses': course_data,
        'projects':project_data,
        'course_total_hours': course_total_hours,
        'project_total_hours': project_total_hours,
        'total_hours_sum': total_hours_sum,
    }


    return render(request, 'total_work.html', context)

def admin_roles(request):
    with connection.cursor() as cursor:
        sql_query = """
            SELECT a.name, ta.credits, ta.alpha, ta.beta, ta.num_students, ta.delta, ta.coordinator, ta.total_hours
            FROM balancer_admin_role AS a
            INNER JOIN balancer_teach_admin_role AS ta ON a.name = ta.role_name
        """
        cursor.execute(sql_query)
        results = cursor.fetchall()

    admin_data = []
    for row in results:
        code = row[0]
        credits = row[1]
        alpha = row[2]
        beta = row[3]
        num_students = row[4]
        delta = row[5]
        coordinator = row[6]
        total_hours = row[7]

        admin = {
            'code': code,
            'credits': credits,
            'alpha': alpha,
            'beta': beta,
            'num_students': num_students,
            'delta': delta,
            'coordinator': coordinator,
            'total_hours': total_hours,
        }

        admin_data.append(admin)
    admin_total_hours = sum(float(admin['total_hours']) for admin in admin_data)
    context = {
        'admin': admin_data,
        'admin_total_hours':admin_total_hours,
    }
    return render(request, 'admin_roles.html',context)

def overall_calcs(request):
    with connection.cursor() as cursor:
        sql_query = """
            SELECT SUM(adjusted_max) FROM balancer_staff
        """
        cursor.execute(sql_query)
        results= cursor.fetchall()
        corestaff_available=results[0][0]
    with connection.cursor() as cursor:
        sql_query = """
            SELECT SUM(total_hours) FROM balancer_teach_course
        """
        cursor.execute(sql_query)
        results= cursor.fetchall()
        course_total=results[0][0]
    with connection.cursor() as cursor:
        sql_query = """
            SELECT SUM(total_hours) FROM balancer_teach_project
        """
        cursor.execute(sql_query)
        results= cursor.fetchall()
        project_total=results[0][0]
    with connection.cursor() as cursor:
        sql_query = """
            SELECT SUM(total_hours) FROM balancer_teach_admin_role
        """
        cursor.execute(sql_query)
        results= cursor.fetchall()
        admin_total=results[0][0]
    total_teaching=course_total+project_total
    total_sum_teach_admin=total_teaching+admin_total

    context={
            'corestaff_available':corestaff_available,   
            'course_total':course_total,
            'project_total':project_total,
            'total_teaching':total_teaching,
            'admin_total':admin_total,
            'total_sum_teach_admin':total_sum_teach_admin,
            }
        
    return render(request, 'overall_calcs.html',context)

def frozen_modules(request):
    return render(request, 'frozen_modules.html')
