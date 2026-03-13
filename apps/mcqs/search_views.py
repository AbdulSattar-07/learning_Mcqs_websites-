"""
Enterprise Search Views
Handles all search-related requests with advanced features
"""

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.db.models import Count
from datetime import datetime
import csv
import json

from .search import AdvancedSearchEngine, SearchAnalytics
from .models import Domain, Topic, Subtopic, Batch


@require_http_methods(["GET"])
def global_search(request):
    """
    Universal search endpoint - searches across all content
    Accessible to all users, but MCQ details require login
    """
    query = request.GET.get('q', '').strip()
    page = request.GET.get('page', 1)
    
    # Get filters
    filters = {
        'domain_id': request.GET.get('domain'),
        'topic_id': request.GET.get('topic'),
        'subtopic_id': request.GET.get('subtopic'),
        'batch_id': request.GET.get('batch'),
        'difficulty': request.GET.get('difficulty'),
        'tag': request.GET.get('tag'),
    }
    
    # Date filters
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    if date_from:
        try:
            filters['date_from'] = datetime.strptime(date_from, '%Y-%m-%d')
        except ValueError:
            pass
    if date_to:
        try:
            filters['date_to'] = datetime.strptime(date_to, '%Y-%m-%d')
        except ValueError:
            pass
    
    # Remove None values
    filters = {k: v for k, v in filters.items() if v}
    
    # Perform search
    user = request.user if request.user.is_authenticated else None
    results = AdvancedSearchEngine.search_all(query, user, filters)
    
    # Paginate MCQs (usually the largest result set)
    mcq_paginator = Paginator(results['mcqs'], 20)
    mcq_page_obj = mcq_paginator.get_page(page)
    
    # Get filter options for UI
    filter_options = {
        'domains': Domain.objects.all().order_by('name'),
        'topics': Topic.objects.all().order_by('name'),
        'subtopics': Subtopic.objects.all().order_by('name'),
        'batches': Batch.objects.all().order_by('name'),
        'difficulties': ['Easy', 'Medium', 'Hard'],
    }
    
    context = {
        'query': query,
        'results': results,
        'mcq_page_obj': mcq_page_obj,
        'filters': filters,
        'filter_options': filter_options,
        'total_results': results['total_results'],
    }
    
    return render(request, 'mcqs/search_results.html', context)


@require_http_methods(["GET"])
def search_suggestions(request):
    """
    AJAX endpoint for search autocomplete suggestions
    Returns JSON with suggested search terms
    """
    query = request.GET.get('q', '').strip()
    limit = int(request.GET.get('limit', 10))
    
    suggestions = AdvancedSearchEngine.get_suggestions(query, limit)
    
    return JsonResponse({
        'query': query,
        'suggestions': suggestions
    })


@require_http_methods(["GET"])
def search_analytics(request):
    """
    View popular searches and search analytics
    Public view to help users discover content
    """
    days = int(request.GET.get('days', 7))
    limit = int(request.GET.get('limit', 20))
    
    popular_searches = SearchAnalytics.get_popular_searches(days, limit)
    
    context = {
        'popular_searches': popular_searches,
        'days': days,
    }
    
    return render(request, 'mcqs/search_analytics.html', context)


@login_required
@require_http_methods(["GET"])
def export_search_results(request):
    """
    Export search results to CSV
    Requires login and MCQ access
    """
    user = request.user
    
    # Check MCQ access
    if not user.has_mcq_access():
        return HttpResponse("Access denied. MCQ access required.", status=403)
    
    query = request.GET.get('q', '').strip()
    
    # Get filters
    filters = {
        'domain_id': request.GET.get('domain'),
        'topic_id': request.GET.get('topic'),
        'subtopic_id': request.GET.get('subtopic'),
        'batch_id': request.GET.get('batch'),
        'difficulty': request.GET.get('difficulty'),
        'tag': request.GET.get('tag'),
    }
    filters = {k: v for k, v in filters.items() if v}
    
    # Get MCQs
    mcqs = AdvancedSearchEngine.search_mcqs(query, filters)
    
    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="search_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'
    
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Domain', 'Topic', 'Subtopic', 'Difficulty', 'Tag', 
        'Question', 'Option A', 'Option B', 'Option C', 'Option D', 
        'Correct Answer', 'Reason', 'Batch', 'Created At'
    ])
    
    for mcq in mcqs:
        writer.writerow([
            mcq.id,
            mcq.domain.name,
            mcq.topic.name,
            mcq.subtopic.name,
            mcq.difficulty,
            mcq.tag,
            mcq.question_text,
            mcq.option_a,
            mcq.option_b,
            mcq.option_c,
            mcq.option_d,
            mcq.correct_answer,
            mcq.reason,
            mcq.batch.name if mcq.batch else '',
            mcq.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    return response


@require_http_methods(["GET"])
def quick_search_api(request):
    """
    Quick search API for AJAX requests
    Returns JSON with limited results for fast response
    """
    query = request.GET.get('q', '').strip()
    search_type = request.GET.get('type', 'all')  # all, domains, topics, subtopics, mcqs
    
    if not query or len(query) < 2:
        return JsonResponse({'error': 'Query too short'}, status=400)
    
    results = {}
    
    if search_type in ['all', 'domains']:
        domains = AdvancedSearchEngine.search_domains(query, limit=5)
        results['domains'] = [
            {
                'id': d.id,
                'name': d.name,
                'topic_count': d.topic_count,
                'mcq_count': d.mcq_count
            } for d in domains
        ]
    
    if search_type in ['all', 'topics']:
        topics = AdvancedSearchEngine.search_topics(query, limit=5)
        results['topics'] = [
            {
                'id': t.id,
                'name': t.name,
                'domain': t.domain.name,
                'subtopic_count': t.subtopic_count,
                'mcq_count': t.mcq_count
            } for t in topics
        ]
    
    if search_type in ['all', 'subtopics']:
        subtopics = AdvancedSearchEngine.search_subtopics(query, limit=5)
        results['subtopics'] = [
            {
                'id': s.id,
                'name': s.name,
                'topic': s.topic.name,
                'domain': s.topic.domain.name,
                'mcq_count': s.mcq_count
            } for s in subtopics
        ]
    
    if search_type in ['all', 'mcqs'] and request.user.is_authenticated:
        mcqs = AdvancedSearchEngine.search_mcqs(query, limit=10)
        results['mcqs'] = [
            {
                'id': m.id,
                'question': m.question_text[:100] + '...' if len(m.question_text) > 100 else m.question_text,
                'domain': m.domain.name,
                'topic': m.topic.name,
                'difficulty': m.difficulty,
                'tag': m.tag
            } for m in mcqs
        ]
    
    return JsonResponse({
        'query': query,
        'results': results
    })
