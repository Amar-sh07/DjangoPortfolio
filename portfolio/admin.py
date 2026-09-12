from django.contrib import admin
from .models import Profile, Skill, Project, Achievement, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "email", "phone", "updated_at")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "created_at")
    ordering = ("order",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "technologies", "order", "created_at")
    ordering = ("order",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "created_at")
    ordering = ("-date",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "message")
    ordering = ("-created_at",)