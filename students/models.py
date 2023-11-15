from django.db import models
from multiselectfield import MultiSelectField

DAYS_OF_THE_WEEK = (
           ("MON", "Понедельник"),
           ("TUE", "Вторник"),
           ("WED", "Среда"),
           ("THU", "Четверг"),
           ("FRI", "Пятница"),
           ("SAT", "Суббота"),
           ("SUN", "Воскресенье")
)


class Student(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50, )
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    student_messenger = models.CharField(verbose_name='Мессенджер студента', max_length=50, null=True, blank=True)
    student_phonenumber = models.CharField(verbose_name='Номер телефона студента', max_length=50, null=True, blank=True)
    parent_name = models.CharField(verbose_name='Имя родителя', max_length=50)
    parent_messenger = models.CharField(verbose_name='Мессенджер родителя', max_length=50)
    parent_phonenumber = models.CharField(verbose_name='Номер телефона родителя', max_length=50)

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lesson(models.Model):
    date = models.DateField(verbose_name='Дата занятия')
    time = models.TimeField(verbose_name='Время занятия')
    done = models.BooleanField(verbose_name='Занятие проведено', default=False)
    video = models.CharField(verbose_name='Видеозапись занятия', max_length=100, null=True, blank=True)
    report = models.CharField(verbose_name='Отчет по занятию', max_length=300, null=True, blank=True)
    homework = models.CharField(verbose_name='Домашнее задание', max_length=300, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "занятие"
        verbose_name_plural = "занятия"

    def __str__(self):
        return f'{self.student} {self.date} {self.time}'


class Schedule(models.Model):
    week_days = MultiSelectField(verbose_name='День недели', max_length=20, choices=DAYS_OF_THE_WEEK)
    time = models.TimeField(verbose_name='Время занятия')
    lessons_left = models.IntegerField(verbose_name='Занятий осталось')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "расписание"
        verbose_name_plural = "расписание"

    def __str__(self):
        return f'{self.student} {self.week_days} {self.time}'
