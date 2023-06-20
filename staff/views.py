from django.shortcuts import get_object_or_404, redirect, render
from .models import Staff
from django.core.paginator import Paginator
import datetime
from django.db.models import Q


def staff_list(request):
    query = request.GET.get('query')
    staff_data = Staff.objects.filter(is_delete=0)

    if query:
        staff_data = staff_data.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(initials__icontains=query)
        )

    paginator = Paginator(staff_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'staff_list.html', {'page_obj': page_obj, 'query': query})


def staff_search(request):
    staff_data = Staff.objects.filter(is_delete=0)
    paginator = Paginator(staff_data, 10)  # Show 10 staff members per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'staff_list.html', {'page_obj': page_obj})


def staff_delete(request, staffId):
    staff = get_object_or_404(Staff, id=staffId)
    staff.is_delete = 1
    staff.save()
    return redirect('staff_list')


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

        # Redirect to the staff list page
        return redirect('/staff/')

    else:
        # Render the staff_add.html template
        return render(request, 'staff_add.html')


def staff_bulk_add(request):
    return render(request, 'staff_bulk_add.html')


def staff_detail(request, staffId):
    staff = get_object_or_404(Staff, id=staffId)
    return render(request, 'staff_detail.html', {'staff': staff})


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

    return redirect('/staff/')
