from django.shortcuts import render
from apps.subjects.models import Grade, Subject, Topic
from .models import Material

def material_filter_view(request):
    grades = Grade.objects.all()
    subjects = Subject.objects.all()
    topics = Topic.objects.all()

    selected_grade_id = request.GET.get('grade')
    selected_subject_id = request.GET.get('subject')
    selected_topic_id = request.GET.get('topic')

    notes = questions = papers = []

    if selected_topic_id:
        notes = Material.objects.filter(topic_id=selected_topic_id, type='notes')
        questions = Material.objects.filter(topic_id=selected_topic_id, type='topical')
        papers = Material.objects.filter(topic_id=selected_topic_id, type='paper')

    context = {
        'grades': grades,
        'subjects': subjects,
        'topics': topics,
        'notes': notes,
        'questions': questions,
        'papers': papers,
        'selected_grade': selected_grade_id,
        'selected_subject': selected_subject_id,
        'selected_topic': selected_topic_id,
    }

    return render(request, 'materials/filter_view.html', context)
