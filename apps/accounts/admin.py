from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from axes.models import AccessAttempt, AccessLog
from .models import CustomUser

# Unregister first
admin.site.unregister(AccessAttempt)
admin.site.unregister(AccessLog)

# Then register with your custom admin
@admin.register(AccessAttempt)
class AccessAttemptAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'failures_since_start', 'attempt_time', 'get_status')
    list_filter = ('failures_since_start', 'attempt_time')
    search_fields = ('username', 'ip_address')

    def get_status(self, obj):
        return "Locked" if obj.failures_since_start >= 5 else "In Progress"
    get_status.short_description = 'Status'

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address',  'attempt_time', 'logout_time')
    search_fields = ('username', 'ip_address')

# Register your custom user
admin.site.register(CustomUser, UserAdmin)
