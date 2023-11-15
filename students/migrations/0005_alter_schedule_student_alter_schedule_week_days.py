# Generated by Django 4.2.7 on 2023-11-15 19:20

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0004_alter_schedule_week_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="schedules",
                to="students.student",
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="week_days",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("MON", "Понедельник"),
                    ("TUE", "Вторник"),
                    ("WED", "Среда"),
                    ("THU", "Четверг"),
                    ("FRI", "Пятница"),
                    ("SAT", "Суббота"),
                    ("SUN", "Воскресенье"),
                ],
                max_length=20,
                verbose_name="День недели",
            ),
        ),
    ]
