from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from .models import CustomUser, ContactRequest, SubscriptionRequest, UserSession
import secrets
import string


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'access_level', 'subscription_status', 'subscription_expiry', 'is_active', 'date_joined']
    list_filter = ['access_level', 'subscription_status', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Subscription Info', {
            'fields': ('access_level', 'subscription_status', 'subscription_expiry')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Subscription Info', {
            'fields': ('email', 'access_level', 'subscription_status', 'subscription_expiry')
        }),
    )


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_processed']
    list_filter = ['is_processed', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    actions = ['mark_as_processed']
    
    def mark_as_processed(self, request, queryset):
        queryset.update(is_processed=True)
    mark_as_processed.short_description = "Mark selected requests as processed"


@admin.register(SubscriptionRequest)
class SubscriptionRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'whatsapp_number', 'package_days', 'status', 'created_at']
    list_filter = ['status', 'package_days', 'created_at']
    search_fields = ['name', 'email', 'whatsapp_number']
    readonly_fields = ['created_at', 'processed_at', 'processed_by']
    
    fieldsets = (
        ('Request Information', {
            'fields': ('name', 'email', 'whatsapp_number', 'package_days')
        }),
        ('Status', {
            'fields': ('status', 'user_account', 'admin_notes')
        }),
        ('Processing Info', {
            'fields': ('created_at', 'processed_at', 'processed_by'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['approve_and_create_account', 'reject_request']
    
    def approve_and_create_account(self, request, queryset):
        """Approve request and create user account with credentials"""
        approved_count = 0
        
        for sub_request in queryset.filter(status='Pending'):
            # Generate username and password
            username = self._generate_username(sub_request.name)
            password = self._generate_password()
            
            # Create user account
            user = CustomUser.objects.create_user(
                username=username,
                email=sub_request.email,
                password=password,
                access_level='Paid',
                subscription_status='Active',
                subscription_expiry=timezone.now().date() + timedelta(days=sub_request.package_days)
            )
            
            # Update subscription request
            sub_request.status = 'Approved'
            sub_request.user_account = user
            sub_request.processed_at = timezone.now()
            sub_request.processed_by = request.user
            sub_request.admin_notes = f"Username: {username}\nPassword: {password}\n\nSend these credentials via WhatsApp: {sub_request.whatsapp_number}"
            sub_request.save()
            
            approved_count += 1
            
            # Display credentials to admin
            messages.success(
                request,
                f"Account created for {sub_request.name}:\n"
                f"Username: {username}\n"
                f"Password: {password}\n"
                f"WhatsApp: {sub_request.whatsapp_number}\n"
                f"Package: {sub_request.get_package_days_display()}\n"
                f"Expires: {user.subscription_expiry}"
            )
        
        if approved_count > 0:
            self.message_user(
                request,
                f'{approved_count} subscription(s) approved. Check admin notes for credentials to send via WhatsApp.',
                messages.SUCCESS
            )
    
    approve_and_create_account.short_description = 'Approve and create user accounts'
    
    def reject_request(self, request, queryset):
        """Reject subscription requests"""
        updated = queryset.filter(status='Pending').update(
            status='Rejected',
            processed_at=timezone.now()
        )
        self.message_user(request, f'{updated} request(s) rejected.')
    
    reject_request.short_description = 'Reject selected requests'
    
    def _generate_username(self, name):
        """Generate unique username from name"""
        base_username = name.lower().replace(' ', '_')[:20]
        username = base_username
        counter = 1
        
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        
        return username
    
    def _generate_password(self, length=12):
        """Generate secure random password"""
        characters = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'session_key_short', 'ip_address', 'login_time', 'last_activity']
    list_filter = ['login_time', 'last_activity']
    search_fields = ['user__username', 'user__email', 'ip_address']
    readonly_fields = ['user', 'session_key', 'ip_address', 'user_agent', 'login_time', 'last_activity']
    
    def session_key_short(self, obj):
        return f"{obj.session_key[:8]}..."
    session_key_short.short_description = 'Session Key'
    
    def has_add_permission(self, request):
        return False
    
    actions = ['force_logout']
    
    def force_logout(self, request, queryset):
        """Force logout users by deleting their session records"""
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f'{count} user(s) forced to logout.')
    force_logout.short_description = 'Force logout selected users'
