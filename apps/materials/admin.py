from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'topic', 'get_subject', 'get_grade', 'uploaded_at')
    list_filter = ('type', 'topic', 'topic__subject', 'topic__subject__grade')

    def get_subject(self, obj):
        return obj.topic.subject
    get_subject.short_description = 'Subject'

    def get_grade(self, obj):
        return obj.topic.subject.grade
    get_grade.short_description = 'Grade'
