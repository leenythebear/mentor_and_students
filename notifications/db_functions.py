from mentors.models import Mentor
from students.models import Lesson
from datetime import datetime, timedelta


def get_today_lessons(mentor_telegram_id):
    mentor = Mentor.objects.get(telegram_id=mentor_telegram_id)
    today_lessons = Lesson.objects.filter(mentor=mentor, date=datetime.now().date())

    return today_lessons


def get_tomorrow_lessons(mentor_telegram_id):
    mentor = Mentor.objects.get(telegram_id=mentor_telegram_id)
    tomorrow_lessons = Lesson.objects.filter(mentor=mentor, date=(datetime.now().date() + timedelta(days=1)))

    return tomorrow_lessons


def get_day_after_tomorrow_lessons(mentor_telegram_id):
    mentor = Mentor.objects.get(telegram_id=mentor_telegram_id)
    tomorrow_lessons = Lesson.objects.filter(mentor=mentor, date=(datetime.now().date() + timedelta(days=2)))

    return tomorrow_lessons
