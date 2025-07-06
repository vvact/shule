from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=20)


    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        ordering = ['name']

    def __str__(self):
        return self.name
   


class Subject(models.Model):
    """Model representing a subject within a grade."""
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='subjects')
    # e.g., Mathematics, English, Science
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        unique_together = ('name',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.name.strip()
    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Topic(models.Model):
    """Model representing a topic within a subject."""
    name = models.CharField(max_length=100)  # e.g., Algebra
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        unique_together = ('name', 'subject')
        ordering = ['name']
