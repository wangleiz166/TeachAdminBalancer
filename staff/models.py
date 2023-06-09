from django.db import models

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    initials = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cat = models.CharField(max_length=50)
    probation = models.CharField(max_length=10, blank=True)
    availability = models.CharField(max_length=50)
    unadjusted_max = models.CharField(max_length=50)
    adjusted_max = models.CharField(max_length=50)
    availability_notes = models.TextField(blank=True)
    empl_end_date = models.DateField(blank=True, null=True)
    probation_start_date = models.DateField(blank=True, null=True)
    probation_start_year_stage = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.id
    
class StaffCourse(models.Model):
    staff_id = models.IntegerField()
    course_id = models.IntegerField()

    def __str__(self):
        return f"{self.staff_id} - {self.course_id}"