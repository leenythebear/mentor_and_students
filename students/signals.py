from django.db.models.signals import post_save
from django.dispatch import receiver

from students.common_helper import get_start_dates, generate_lessons
from students.models import Schedule, Lesson


@receiver(post_save, sender=Schedule)
def create_related_objects(sender, instance, created, **kwargs):
    if created:
        start_dates = get_start_dates(instance)
        dates = generate_lessons(instance.lessons_left, start_dates)
        for date in dates:
            Lesson.objects.create(date=date, time=instance.time, student=instance.student)