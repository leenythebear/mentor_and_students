from datetime import datetime, timedelta

from mentor_and_students.common.fields import IterableMSFListWrapper


def get_start_dates(schedule):
    week_days_order = {
        "MON": 0,
        "TUE": 1,
        "WED": 2,
        "THU": 3,
        "FRI": 4,
        "SAT": 5,
        "SUN": 6
    }

    today = datetime.now().date()  # use django tzlib

    start_dates = []

    for week_day in schedule.week_days:
        week_day_number = week_days_order[week_day]
        days_until_target_day = (week_day_number - today.weekday() + 7) % 7
        if days_until_target_day == 0:
            days_until_target_day = 7
        target_date = today + timedelta(days=days_until_target_day)
        start_dates.append(target_date)
    return start_dates


def generate_lessons(lessons_left, start_dates):
    lessons_dates = start_dates.copy()
    while len(lessons_dates) < lessons_left:
        for start_date in start_dates:
            next_date = start_date + timedelta(days=7)
            lessons_dates.append(next_date)
            start_dates = lessons_dates[-2:]
            if len(lessons_dates) == lessons_left:
                break

    return lessons_dates
