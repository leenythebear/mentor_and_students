from django.contrib import admin

from mentors.models import Mentor


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    search_fields = [
        "first_name",
        "last_name"
    ]
    list_display = [
        "first_name",
        "last_name",
    ]
