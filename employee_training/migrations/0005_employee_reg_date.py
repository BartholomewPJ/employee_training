# Generated by Django 5.1.5 on 2025-01-21 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_training', '0004_employee_priority_alter_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='reg_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Data Registration Date'),
        ),
    ]
