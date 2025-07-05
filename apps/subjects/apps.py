from django.apps import AppConfig


class SubjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.subjects'
    verbose_name = 'Subjects Management'
    label = 'subjects'
    def ready(self):
        # Import signals or any other startup code here
        try:
            import apps.subjects.signals  # Ensure signals are imported
        except ImportError:
            pass  # Handle the case where signals module does not exist
