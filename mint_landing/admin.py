from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin

from .models import FAQ, AboutUs, Announcement, ContactUs, HeroSection, NumberStatistic, Project


admin.site.unregister(User)
admin.site.unregister(Group)


def toggle_active_status(modeladmin, request, queryset):
    for user in queryset:
        user.is_active = not user.is_active
        user.save()
    modeladmin.message_user(
        request, "Selected users' active status has been toggled.")


toggle_active_status.short_description = "Toggle active status of selected users"


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    actions = [toggle_active_status]
    list_display = ["username", "first_name",
                    "last_name", "email", "date_joined", "is_active"]


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(HeroSection)
class HeroSectionAdmin(ModelAdmin):
    list_display = ["title", "subtitle",
                    "button_text", "created_at", "updated_at"]
    search_fields = ["title", "subtitle", "button_text"]
    list_filter = ["created_at", "updated_at"]


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'button_url', 'updated_at',
                    'is_active', 'updated_at')
    list_filter = ('updated_at',)
    search_fields = ('title', 'description', 'button_text')


@admin.register(Announcement)
class AnnouncementAdmin(ModelAdmin):
    list_display = ('title', 'sub_title', 'updated_at')
    search_fields = ('title', 'sub_title', 'description')


@admin.register(AboutUs)
class AboutUsAdmin(ModelAdmin):
    list_display = ['title', 'updated_at']
    search_fields = ['title', 'description_1',
                     'description_2', 'bullet_points']
    list_filter = ['updated_at']


@admin.register(NumberStatistic)
class NumberStatisticAdmin(ModelAdmin):
    list_display = ['title', 'value', 'updated_at']
    search_fields = ['title', 'value']
    list_filter = ['title', 'value', 'updated_at']


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ['question', 'answer', 'order']
    search_fields = ['question', 'answer']


@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ['title', 'address', 'email', 'phone', 'updated_at']
