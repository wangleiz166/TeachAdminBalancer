# Generated by Django 4.1.2 on 2023-06-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffvModules', '0002_course_schoolrole_teachadminrole_teachcourse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
