# Generated by Django 3.0 on 2024-12-21 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_course_college'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facilities',
            name='COLLEGE',
        ),
    ]
