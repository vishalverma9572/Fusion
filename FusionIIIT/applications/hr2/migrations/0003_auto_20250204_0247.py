# Generated by Django 3.1.5 on 2025-02-04 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr2', '0002_leaveform_attached_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavebalance',
            name='id',
        ),
        migrations.RemoveField(
            model_name='leaveperyear',
            name='id',
        ),
        migrations.AlterField(
            model_name='leavebalance',
            name='empid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='leave_balance', serialize=False, to='hr2.employee'),
        ),
        migrations.AlterField(
            model_name='leaveperyear',
            name='empid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='yearly_leave', serialize=False, to='hr2.employee'),
        ),
    ]
