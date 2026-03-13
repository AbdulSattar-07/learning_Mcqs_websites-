from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    ACCESS_LEVEL_CHOICES = [
        ('Free', 'Free'),
        ('Paid', 'Paid'),
    ]
    
    SUBSCRIPTION_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
        ('Inactive', 'Inactive'),
    ]
    
    email = models.EmailField(unique=True)
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVEL_CHOICES, default='Free')
    subscription_status = models.CharField(max_length=20, choices=SUBSCRIPTION_STATUS_CHOICES, default='Inactive')
    subscription_expiry = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'custom_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username
    
    def has_mcq_access(self):
        """Check if user has valid MCQ access"""
        if not self.is_active:
            return False
        if self.access_level != 'Paid':
            return False
        if self.subscription_status != 'Active':
            return False
        if self.subscription_expiry and self.subscription_expiry < timezone.now().date():
            return False
        return True


class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'contact_request'
        ordering = ['-created_at']
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'
    
    def __str__(self):
        return f"{self.name} - {self.email}"


class SubscriptionRequest(models.Model):
    PACKAGE_CHOICES = [
        (7, '7 Days'),
        (15, '15 Days'),
        (30, '30 Days'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp_number = models.CharField(max_length=20)
    package_days = models.IntegerField(choices=PACKAGE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    processed_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='processed_requests')
    user_account = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='subscription_request')
    admin_notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'subscription_request'
        ordering = ['-created_at']
        verbose_name = 'Subscription Request'
        verbose_name_plural = 'Subscription Requests'
    
    def __str__(self):
        return f"{self.name} - {self.get_package_days_display()} - {self.status}"


class UserSession(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='active_session')
    session_key = models.CharField(max_length=40, unique=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    login_time = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_session'
        verbose_name = 'User Session'
        verbose_name_plural = 'User Sessions'
    
    def __str__(self):
        return f"{self.user.username} - {self.session_key[:8]}..."
