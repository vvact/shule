from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=20,unique=True)  # e.g., Grade 6, Form 1

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        ordering = ['name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    """Model representing a subject within a grade."""
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        unique_together = ('name', 'grade')

    def __str__(self):
        return f"{self.name} ({self.grade.name})"  # ✅ e.g. Math (Grade 6)


class Topic(models.Model):
    """Model representing a topic within a subject."""
    name = models.CharField(max_length=100)  # e.g., Algebra
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.subject.name} - {self.subject.grade.name})"  # ✅ e.g. Fractions (Math - Grade 6)

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        unique_together = ('name', 'subject')
        ordering = ['name']