from django.db import models

class Staff(models.Model):
    initials = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)
    probation_year = models.CharField(max_length=10)
    annual_availability = models.IntegerField()
    unadjusted_max = models.IntegerField()
    adjusted_max = models.IntegerField()
    availability_notes = models.TextField()
    employment_end_date = models.DateField()
    probation_start_date = models.DateField()
    probation_start_year_stage = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.initials} - {self.first_name} {self.last_name}"

    class Meta:
        db_table = 'balancer_staff'