# Generated by Django 5.1.4 on 2025-01-16 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_teammembership_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='name',
            new_name='role',
        ),
    ]
