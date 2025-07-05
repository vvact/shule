# apps/accounts/views.py

from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomLoginForm
from django.shortcuts import render, redirect
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Show success message with loading effect
            messages.success(request, 'Account created successfully!')
            return render(request, 'accounts/register.html', {
                'form': form,
                'show_loading': True,  # Flag to show loading animation
                'user_email': user.email  # Pass email for success message
            })
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        # Check "remember me" from the form
        remember_me = form.cleaned_data.get('remember_me')

        # Log in the user
        response = super().form_valid(form)

        if remember_me:
            # Set session to expire in 2 weeks (or whatever you want)
            self.request.session.set_expiry(1209600)  # 2 weeks in seconds
        else:
            # Session will expire when browser is closed
            self.request.session.set_expiry(0)

    

        # Show loading effect
        return render(self.request, 'accounts/login.html', {
            'show_loading': True,
            'redirect_to': self.get_success_url()
        })

class DashboardView(TemplateView):
    template_name = 'accounts/dashboard.html'
