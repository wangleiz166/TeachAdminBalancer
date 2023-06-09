from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    identity = models.IntegerField(choices=((1, 'Manager'), (2, 'Employee'), (3, 'IT Administrator')))
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Permission(models.Model):
    menu_id = models.IntegerField()
    permission = models.IntegerField(choices=((0, 'No Access'), (1, 'View'), (2, 'Edit'), (3, 'Full Access')))
    user_id = models.IntegerField()

    def __str__(self):
        return f"User ID: {self.user_id} - Menu ID: {self.menu_id}"

class Log(models.Model):
    user_id = models.IntegerField()
    operation = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User ID: {self.user_id} - {self.operation}"

