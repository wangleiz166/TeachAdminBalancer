from django.db import models

class TeachCourse(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField()
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    alpha = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    num_students = models.IntegerField()
    delta = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    total_hours = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'balancer_teach_course'

class TeachProject(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField()
    project_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    alpha = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    num_students = models.IntegerField()
    delta = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    total_hours = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name
    
    class Meta:
        db_table = 'balancer_teach_project'

class TeachAdminRole(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField()
    role_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    alpha = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    num_students = models.IntegerField()
    delta = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    total_hours = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.role_name
    
    class Meta:
        db_table = 'balancer_teach_admin_role'


class TeachSchoolRoles(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField()
    role_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    alpha = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    num_students = models.IntegerField()
    delta = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    total_hours = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.role_name
    
    class Meta:
        db_table = 'balancer_teach_school_role'

class TeachUniRoles(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField()
    role_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    alpha = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    num_students = models.IntegerField()
    delta = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    total_hours = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.role_name
    
    class Meta:
        db_table = 'balancer_teach_uni_role'

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    linked_courses = models.CharField(max_length=100)
    unlinked_relatives = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True, blank=True)
    hs = models.CharField(max_length=100, null=True, blank=True)
    num_staff_allocated = models.IntegerField()
    est_num_students = models.IntegerField()
    hours = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'balancer_course'

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    linked_courses = models.CharField(max_length=100)
    unlinked_relatives = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True, blank=True)
    num_staff_allocated = models.IntegerField()
    est_num_students = models.IntegerField()
    hours = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'balancer_project'


class AdminRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    num_staff_allocated = models.IntegerField()
    crit = models.IntegerField()
    hours = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'balancer_admin_role'


class SchoolRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    crit = models.IntegerField()
    hours = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'balancer_school_role'

class UniRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    crit = models.IntegerField()
    hours = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'balancer_uni_role' 