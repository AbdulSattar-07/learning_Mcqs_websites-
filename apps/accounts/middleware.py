from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import UserSession


class SingleDeviceLoginMiddleware:
    """
    Middleware to enforce single device login policy.
    If a user logs in from a new device, the old session is terminated.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            current_session_key = request.session.session_key
            
            try:
                user_session = UserSession.objects.get(user=request.user)
                
                # Check if current session matches stored session
                if user_session.session_key != current_session_key:
                    # User is logged in from another device
                    logout(request)
                    messages.warning(
                        request,
                        'Your account has been logged in from another device. '
                        'Only one active session is allowed at a time.'
                    )
                    return redirect('accounts:login')
                
                # Update last activity
                user_session.save()
                
            except UserSession.DoesNotExist:
                # Session record doesn't exist, log out user
                logout(request)
                messages.warning(request, 'Session expired. Please login again.')
                return redirect('accounts:login')
        
        response = self.get_response(request)
        return response
