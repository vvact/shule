from django.shortcuts import render
from apps.subjects.models import Grade, Subject


# Create your views here.
def home(request):
    grades = Grade.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'core/home.html', {
        'grades': grades,
        'subjects': subjects,
    })

def about(request):
    """
    Render the about page.
    """
    return render(request, 'core/about.html')
    
def contact(request):
    """
    Render the contact page.
    """
    return render(request, 'core/contact.html')
