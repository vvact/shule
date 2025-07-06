from django.contrib import admin

# Register your models here.
from .models import Grade, Subject, Topic
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'name': ('name',)}
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    search_fields = ('name', 'subject__name')
    ordering = ('name',)
    prepopulated_fields = {'name': ('name',)}
    list_filter = ('subject',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('subject')
    def subject(self, obj):
        return obj.subject.name if obj.subject else 'No Subject'
    subject.admin_order_field = 'subject__name'
    subject.short_description = 'Subject Name'
admin.site.site_header = 'Subjects Management'
admin.site.site_title = 'Subjects Admin'
admin.site.index_title = 'Subjects Administration'
admin.site.site_url = '/admin/'  # Set the admin site URL to the default admin page
