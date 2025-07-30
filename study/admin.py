from django.contrib import admin
from .models import Grade, Subject, Topic, TopicalQuestion, Note

# Inline Notes and Topical Questions under Topic
class NoteInline(admin.StackedInline):
    model = Note
    extra = 1

class TopicalQuestionInline(admin.StackedInline):
    model = TopicalQuestion
    extra = 1

# Inline Topics under Subject
class TopicInline(admin.StackedInline):
    model = Topic
    extra = 1

# Inline Subjects under Grade
class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 1

# Admin for Grade with inline Subjects
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    list_display = ['name']
    search_fields = ['name']

# Admin for Subject with inline Topics
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [TopicInline]
    list_display = ['name', 'grade']
    list_filter = ['grade']
    search_fields = ['name']

# Admin for Topic with inline Notes and Questions
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = [NoteInline, TopicalQuestionInline]
    list_display = ['title', 'subject']
    list_filter = ['subject']
    search_fields = ['title']

# Optional: Admin for Notes
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic']
    list_filter = ['topic']
    search_fields = ['title']

# Optional: Admin for Topical Questions
@admin.register(TopicalQuestion)
class TopicalQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'difficulty', 'topic']
    list_filter = ['difficulty', 'topic']
    search_fields = ['question']





# Branding the Admin Panel
admin.site.site_header = "📘 EdTech Platform Admin"
admin.site.site_title = "EdTech Admin Portal"
admin.site.index_title = "Welcome to the EdTech Content Manager"



from django.contrib import admin
from django.contrib.admin import AdminSite

# Optional: Change admin header/title
admin.site.site_header = "My EdTech PlatformAdmin"
admin.site.site_title = "My EdTech Admin Portal"
admin.site.index_title = "Welcome to the Admin Dashboard"

# Inject custom CSS
class MyAdminSite(AdminSite):
    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }

# Or globally using admin site overrides (best for global style)
admin.site.enable_nav_sidebar = False  # Optional: hide nav sidebar

# Optional: if using custom login template/logo, override templates as well

