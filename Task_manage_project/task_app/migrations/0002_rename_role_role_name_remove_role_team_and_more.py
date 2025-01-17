# Generated by Django 5.1.4 on 2025-01-16 07:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='role',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='role',
            name='team',
        ),
        migrations.RemoveField(
            model_name='role',
            name='user',
        ),
        migrations.CreateModel(
            name='TeamMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task_app.role')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
