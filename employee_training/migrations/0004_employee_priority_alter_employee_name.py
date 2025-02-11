# Generated by Django 5.1.5 on 2025-01-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_training', '0003_division_in_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='priority',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1, verbose_name='Learning Priorities'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Employee Name'),
        ),
    ]
