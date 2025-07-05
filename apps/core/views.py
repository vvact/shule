from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page.
    """
    return render(request, 'core/home.html')

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
