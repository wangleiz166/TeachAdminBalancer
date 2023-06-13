from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    mail = models.EmailField()
    pass_word = models.CharField(max_length=100)
    permission_id = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f"User {self.user_name}"

    class Meta:
        db_table = 'balancer_user'


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    position_id = models.IntegerField()
    menu_id = models.IntegerField()
    permission = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id} - {self.menu_id}"

    class Meta:
        db_table = 'balancer_permission'


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    operation_details = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - User ID: {self.user_id}"

    class Meta:
        db_table = 'balancer_log'