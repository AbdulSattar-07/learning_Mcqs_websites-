from django.urls import path
from . import views, search_views

app_name = 'mcqs'

urlpatterns = [
    # Content browsing
    path('domains/', views.domain_list, name='domain_list'),
    path('topics/', views.topic_list, name='topic_list'),
    path('topics/domain/<int:domain_id>/', views.topic_list, name='topic_list_by_domain'),
    path('subtopics/', views.subtopic_list, name='subtopic_list'),
    path('subtopics/topic/<int:topic_id>/', views.subtopic_list, name='subtopic_list_by_topic'),
    path('mcqs/', views.mcq_list, name='mcq_list'),
    path('mcqs/<int:mcq_id>/', views.mcq_detail, name='mcq_detail'),
    
    # Enterprise search features
    path('search/', search_views.global_search, name='global_search'),
    path('search/suggestions/', search_views.search_suggestions, name='search_suggestions'),
    path('search/analytics/', search_views.search_analytics, name='search_analytics'),
    path('search/export/', search_views.export_search_results, name='export_search'),
    path('api/search/', search_views.quick_search_api, name='quick_search_api'),
]
