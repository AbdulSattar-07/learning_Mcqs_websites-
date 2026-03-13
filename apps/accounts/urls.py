from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.ContactRequestView.as_view(), name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('get-access/', views.SubscriptionRequestView.as_view(), name='subscription_request'),
    path('subscription/success/', views.subscription_success, name='subscription_success'),
    path('test-whatsapp/', views.test_whatsapp, name='test_whatsapp'),
]
