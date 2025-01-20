# Generated by Django 5.1.4 on 2025-01-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_rename_name_role_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='Medium', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('to do', 'To Do'), ('pending', 'Pending'), ('in progress', 'In Progress'), ('completed', 'Completed'), ('in review', 'In Review')], default='Not Started', max_length=200),
        ),
    ]
