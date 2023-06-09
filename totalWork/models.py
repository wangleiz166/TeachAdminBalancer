from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credits = models.CharField(max_length=10)
    cat = models.CharField(max_length=50)
    num_staff_allocated = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.id
