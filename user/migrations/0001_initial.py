# Generated by Django 4.1.2 on 2023-06-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('operation_details', models.CharField(max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'balancer_log',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('position_id', models.IntegerField()),
                ('menu_id', models.IntegerField()),
                ('permission', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'balancer_permission',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('pass_word', models.CharField(max_length=100)),
                ('permission_id', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'balancer_user',
            },
        ),
    ]
