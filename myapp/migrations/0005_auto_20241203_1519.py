# Generated by Django 3.0 on 2024-12-03 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20241203_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccancy_skill',
            old_name='VACANCY',
            new_name='VACCANCY',
        ),
    ]
