from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session
from .forms import CustomLoginForm, ContactRequestForm, SubscriptionRequestForm
from .models import UserSession


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        
        # Check if user already has an active session
        if not user.is_superuser:
            try:
                existing_session = UserSession.objects.get(user=user)
                # Delete the old session from Django's session table
                try:
                    old_session = Session.objects.get(session_key=existing_session.session_key)
                    old_session.delete()
                except Session.DoesNotExist:
                    pass
                # Delete the UserSession record
                existing_session.delete()
            except UserSession.DoesNotExist:
                pass
        
        # Login the user
        login(self.request, user)
        
        # Create new session record for non-superusers
        if not user.is_superuser:
            # Get client IP
            x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[0]
            else:
                ip_address = self.request.META.get('REMOTE_ADDR')
            
            # Get user agent
            user_agent = self.request.META.get('HTTP_USER_AGENT', '')
            
            # Create session record
            UserSession.objects.create(
                user=user,
                session_key=self.request.session.session_key,
                ip_address=ip_address,
                user_agent=user_agent
            )
        
        messages.success(self.request, f'Welcome back, {user.username}!')
        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)


def logout_view(request):
    # Delete user session record if exists
    if request.user.is_authenticated and not request.user.is_superuser:
        try:
            user_session = UserSession.objects.get(user=request.user)
            user_session.delete()
        except UserSession.DoesNotExist:
            pass
    
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')


class ContactRequestView(CreateView):
    form_class = ContactRequestForm
    template_name = 'accounts/contact.html'
    success_url = reverse_lazy('accounts:contact_success')
    
    def form_valid(self, form):
        messages.success(self.request, 'Your request has been submitted. The administrator will contact you soon.')
        return super().form_valid(form)


def contact_success(request):
    return render(request, 'accounts/contact_success.html')


class SubscriptionRequestView(CreateView):
    form_class = SubscriptionRequestForm
    template_name = 'accounts/subscription_request.html'
    success_url = reverse_lazy('accounts:subscription_success')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            'Your subscription request has been submitted! '
            'Admin will contact you on WhatsApp with your login credentials.'
        )
        return super().form_valid(form)


def subscription_success(request):
    return render(request, 'accounts/subscription_success.html')
def test_whatsapp(request):
    return render(request, 'test_whatsapp.html')


def test_whatsapp(request):
    return render(request, 'test_whatsapp.html')
