from django.contrib import admin
from .models import Fish
from .forms import FishForm
from django.contrib.admin.models import LogEntry
# Register your models here.


class FishAdmin(admin.ModelAdmin):
    form = FishForm


admin.site.register(Fish, FishAdmin)

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        queryset.delete()

    def has_delete_permission(self, request, obj=None):
        # Limit delete permission to superusers only
        return request.user.is_superuser

    delete_selected.short_description = "Delete selected recent actions"




