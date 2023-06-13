from django.db import models

class Teach(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    alpha = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    num_students = models.IntegerField()
    delta = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    total_hours = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'balancer_teach'

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    alpha = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    num_students = models.IntegerField()
    delta = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    total_hours = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name
    
    class Meta:
        db_table = 'balancer_project'

class AdminRole(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    alpha = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    num_students = models.IntegerField()
    delta = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    total_hours = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.role_name
    
    class Meta:
        db_table = 'balancer_admin_role'

class StaffRelation(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField()
    teach_id = models.IntegerField()
    project_id = models.IntegerField()
    admin_role_jd = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
            return f"StaffRelation {self.id}"
    
    class Meta:
        db_table = 'balancer_staff_relaction'