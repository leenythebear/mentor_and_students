# Generated by Django 4.2.7 on 2023-11-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0005_alter_schedule_student_alter_schedule_week_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="students.student"
            ),
        ),
    ]
