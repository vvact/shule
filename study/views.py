from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Grade, Subject, Topic, Note, TopicalQuestion
from .serializers import (
    GradeSerializer, SubjectSerializer, TopicSerializer,
    NoteSerializer, TopicalQuestionSerializer
)

# 🔹 Reusable Base ViewSet for Filtering
class BaseFilterViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class SubjectViewSet(BaseFilterViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filterset_fields = ['grade']  # 🔍 Filter subjects by grade

class TopicViewSet(BaseFilterViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filterset_fields = ['subject']

class NoteViewSet(BaseFilterViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filterset_fields = ['topic']

class TopicalQuestionViewSet(BaseFilterViewSet):
    queryset = TopicalQuestion.objects.all()
    serializer_class = TopicalQuestionSerializer
    filterset_fields = ['topic', 'difficulty']



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Note, TopicalQuestion, Topic, Subject
from .serializers import (
    NoteSerializer, TopicalQuestionSerializer,
    TopicSerializer, SubjectSerializer
)

class GlobalSearchView(APIView):
    def get(self, request):
        query = request.GET.get("q")
        if not query:
            return Response(
                {"detail": "Query parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({
            "notes": NoteSerializer(
                Note.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)),
                many=True
            ).data,
            "questions": TopicalQuestionSerializer(
                TopicalQuestion.objects.filter(Q(question__icontains=query) | Q(answer__icontains=query)),
                many=True
            ).data,
            "topics": TopicSerializer(
                Topic.objects.filter(Q(title__icontains=query)),
                many=True
            ).data,
            "subjects": SubjectSerializer(
                Subject.objects.filter(Q(name__icontains=query)),
                many=True
            ).data,
        })
