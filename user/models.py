# INSERT INTO "main"."balancer_permission" ("id", "user_id", "position_id", "menu_id", "permission", "create_time", "is_delete") VALUES
#   -- Manager Permissions
#   (1, 0, 1, 1, 'Manager', CURRENT_TIMESTAMP, 0),
#   (2, 0, 1, 2, 'Manager', CURRENT_TIMESTAMP, 0),
#   (3, 0, 1, 3, 'Manager', CURRENT_TIMESTAMP, 0),
#   (4, 0, 1, 4, 'Manager', CURRENT_TIMESTAMP, 0),
#   (5, 0, 1, 5, 'Manager', CURRENT_TIMESTAMP, 0),
#   (6, 0, 1, 6, 'Manager', CURRENT_TIMESTAMP, 0),

#   -- Employee Permissions
#   (7, 0, 1, 1, 'Employee', CURRENT_TIMESTAMP, 0),
#   (8, 0, 1, 2, 'Employee', CURRENT_TIMESTAMP, 0),
#   (9, 0, 1, 3, 'Employee', CURRENT_TIMESTAMP, 0),
#   (10, 0, 1, 4, 'Employee', CURRENT_TIMESTAMP, 0),
#   (11, 0, 1, 5, 'Employee', CURRENT_TIMESTAMP, 0),
#   (12, 0, 1, 6, 'Employee', CURRENT_TIMESTAMP, 0),

#   -- IT Administrator Permissions
#   (13, 0, 1, 1, 'IT Administrator', CURRENT_TIMESTAMP, 0),
#   (14, 0, 1, 2, 'IT Administrator', CURRENT_TIMESTAMP, 0),
#   (15, 0, 1, 3, 'IT Administrator', CURRENT_TIMESTAMP, 0),
#   (16, 0, 1, 4, 'IT Administrator', CURRENT_TIMESTAMP, 0),
#   (17, 0, 1, 5, 'IT Administrator', CURRENT_TIMESTAMP, 0),
#   (18, 0, 1, 6, 'IT Administrator', CURRENT_TIMESTAMP, 0);

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    mail = models.EmailField()
    pass_word = models.CharField(max_length=100)
    permission_id = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    login_attempts = models.IntegerField(default=0)
    locked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"User {self.user_name}"

    class Meta:
        db_table = 'balancer_user'


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    position_id = models.IntegerField()
    menu_id = models.IntegerField()
    permission = models.CharField(max_length=100)
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

    @classmethod
    def create_log(cls, user_id, operation_details):
        log = cls(user_id=user_id, operation_details=operation_details)
        log.save()