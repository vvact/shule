from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GradeViewSet, SubjectViewSet, TopicViewSet,
    NoteViewSet, TopicalQuestionViewSet,
    GlobalSearchView
)

router = DefaultRouter()
router.register(r'grades', GradeViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'topical-questions', TopicalQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', GlobalSearchView.as_view(), name='global-search'),
]
