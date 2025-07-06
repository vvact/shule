from django.contrib import admin

# Register your models here.
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'topic', 'uploaded_at')
    list_filter = ('type', 'topic', 'topic__subject')
