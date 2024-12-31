from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin


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
