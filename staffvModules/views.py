
from django.shortcuts import get_object_or_404,render, redirect
from .models import Course,Project,AdminRole,SchoolRole,UniRole
from django.core.paginator import Paginator

# Create your views here.

def list(request):
    # Retrieve all non-deleted courses from the database
    courses = Course.objects.filter(is_delete=0)

    # Search functionality
    query = request.GET.get('query')
    if query:
        # Filter courses based on the search query and is_delete condition
        courses = courses.filter(code__icontains=query)

    # Pagination
    paginator = Paginator(courses, 10)  # Show 10 courses per page
    page_number = request.GET.get('page')
    courses = paginator.get_page(page_number)

    # Pass the courses, search query, and pagination to the template
    context = {'courses': courses, 'query': query}
    return render(request, 'list.html', context)

def full_list(request, category=None):
    # Retrieve all non-deleted items from the database based on the category
    if category == 'project':
        items = Project.objects.filter(is_delete=0)
        template_name = 'full/full_project_list.html'
    elif category == 'adminrole':
        items = AdminRole.objects.filter(is_delete=0)
        template_name = 'full/full_adminrole_list.html'
    elif category == 'schoolrole':
        items = SchoolRole.objects.filter(is_delete=0)
        template_name = 'full/full_schoolrole_list.html'
    elif category == 'unirole':
        items = UniRole.objects.filter(is_delete=0)
        template_name = 'full/full_unirole_list.html'
    else:
        items = Course.objects.filter(is_delete=0)
        template_name = 'full/full_course_list.html'
    
    context = {'list': items}
    return render(request, template_name, context)

    

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

def detail(request):
    return render(request, 'detail.html')

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

        # Redirect to the staffvModules list page
        return redirect('/staffvModules/')

    # Pass the course object to the template
    context = {'course': course}
    return render(request, 'staffvModules_course_edit.html', context)

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

        return redirect('/staffvModules/')

    return render(request, 'staffvModules_course_add.html')


def staffvModules_course_del(request, courseId):
    course = get_object_or_404(Course, id=courseId)
    course.is_delete = 1
    course.save()
    return redirect('/staffvModules/')


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

        # Redirect to the staffvModules project list page
        return redirect('/staffvModules/project/')

    # Pass the project object to the template
    context = {'project': project}
    return render(request, 'staffvModules_project_edit.html', context)


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

        return redirect('/staffvModules/project/')

    return render(request, 'staffvModules_project_add.html')


def staffvModules_project_del(request, projectId):
    project = get_object_or_404(Project, id=projectId)
    project.is_delete = 1
    project.save()
    return redirect('/staffvModules/project/')



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

        # Redirect to the staffvModules list page
        return redirect('/staffvModules/adminRole/')

    # Pass the course object to the template
    context = {'adminrole': adminrole}
    return render(request, 'staffvModules_adminrole_edit.html', context)

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

        return redirect('/staffvModules/adminRole/')

    return render(request, 'staffvModules_adminrole_add.html')

def staffvModules_adminrole_del(request, adminroleId):
    adminrole = get_object_or_404(AdminRole, id=adminroleId)
    adminrole.is_delete = 1
    adminrole.save()
    return redirect('/staffvModules/adminRole/')


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

        # Redirect to the staffvModules list page
        return redirect('/staffvModules/schoolRole/')

    # Pass the course object to the template
    context = {'schoolrole': schoolrole}
    return render(request, 'staffvModules_schoolrole_edit.html', context)

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

        return redirect('/staffvModules/schoolRole/')

    return render(request, 'staffvModules_schoolrole_add.html')

def staffvModules_schoolrole_del(request, schoolroleId):
    schoolrole = get_object_or_404(SchoolRole, id=schoolroleId)
    schoolrole.is_delete = 1
    schoolrole.save()
    return redirect('/staffvModules/schoolRole/')



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

        # Redirect to the staffvModules list page
        return redirect('/staffvModules/uniRole/')

    # Pass the course object to the template
    context = {'unirole': unirole}
    return render(request, 'staffvModules_unirole_edit.html', context)

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

        return redirect('/staffvModules/uniRole/')

    return render(request, 'staffvModules_unirole_add.html')

def staffvModules_unirole_del(request, uniroleId):
    unirole = get_object_or_404(UniRole, id=uniroleId)
    unirole.is_delete = 1
    unirole.save()
    return redirect('/staffvModules/uniRole/')

