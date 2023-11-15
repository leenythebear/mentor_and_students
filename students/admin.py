from django.contrib import admin

from students.models import Student, Schedule, Lesson


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = [
        "first_name",
        "last_name"
    ]
    list_display = [
        "first_name",
        "last_name",
        "date_of_birth",
        "parent_name",
    ]
    inlines = [ScheduleInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    search_fields = [
        "date",
        "time",
        "done"
    ]
    list_display = [
        "date",
        "time",
        "student"
    ]
