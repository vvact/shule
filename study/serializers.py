from rest_framework import serializers
from .models import Grade, Subject, Topic, Note, TopicalQuestion

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class TopicalQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicalQuestion
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    questions = TopicalQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Grade
        fields = '__all__'
