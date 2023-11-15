# Generated by Django 4.2.7 on 2023-11-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_alter_student_first_name_alter_student_last_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="schedule",
            options={"verbose_name": "расписание", "verbose_name_plural": "расписание"},
        ),
        migrations.AlterField(
            model_name="lesson",
            name="date",
            field=models.DateField(verbose_name="Дата занятия"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="done",
            field=models.BooleanField(default=False, verbose_name="Занятие проведено"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="homework",
            field=models.CharField(
                blank=True, max_length=300, null=True, verbose_name="Домашнее задание"
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="report",
            field=models.CharField(
                blank=True, max_length=300, null=True, verbose_name="Отчет по занятию"
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="time",
            field=models.TimeField(verbose_name="Время занятия"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="video",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="Видеозапись занятия",
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="lessons_left",
            field=models.IntegerField(verbose_name="Занятий осталось"),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="time",
            field=models.TimeField(verbose_name="Время занятия"),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="week_days",
            field=models.CharField(
                choices=[
                    ("ПНД", "Понедельник"),
                    ("ВТ", "Вторник"),
                    ("СР", "Среда"),
                    ("ЧТ", "Четверг"),
                    ("ПТ", "Пятница"),
                    ("СБ", "Суббота"),
                    ("ВСКР", "Воскресенье"),
                ],
                max_length=20,
                verbose_name="День недели",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True, verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="student",
            name="first_name",
            field=models.CharField(max_length=50, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="student",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Фамилия"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="parent_messenger",
            field=models.CharField(max_length=50, verbose_name="Мессенджер родителя"),
        ),
        migrations.AlterField(
            model_name="student",
            name="parent_name",
            field=models.CharField(max_length=50, verbose_name="Имя родителя"),
        ),
        migrations.AlterField(
            model_name="student",
            name="parent_phonenumber",
            field=models.CharField(
                max_length=50, verbose_name="Номер телефона родителя"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_messenger",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Мессенджер студента"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_phonenumber",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Номер телефона студента",
            ),
        ),
    ]
