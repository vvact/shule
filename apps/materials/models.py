# materials/models.py
from django.db import models
from ckeditor.fields import RichTextField
from apps.subjects.models import Topic


NOTES = 'notes'
TOPICAL = 'topical'
PAPER = 'paper'

class Material(models.Model):
    MATERIAL_TYPE = (
        (NOTES, 'Notes'),
        (TOPICAL, 'Topical Questions'),
        (PAPER, 'Past Paper'),
    )

    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=MATERIAL_TYPE)
    content = RichTextField(blank=True, null=True)  # Text content (view-only)
    embed_url = models.URLField(blank=True, null=True)  # For PDFs or Google Drive view
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ['-uploaded_at']
