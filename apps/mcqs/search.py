"""
Enterprise-Level Advanced Search System
Supports multi-field search with intelligent ranking, fuzzy matching, and analytics
"""

from django.db.models import Q, Count, Case, When, IntegerField, Value, CharField
from django.db.models.functions import Lower, Concat
from django.core.cache import cache
from django.utils import timezone
from datetime import timedelta
from .models import Domain, Topic, Subtopic, MCQ, Batch
import re


class SearchAnalytics:
    """Track and analyze search patterns"""
    
    @staticmethod
    def log_search(query, user=None, results_count=0):
        """Log search query for analytics"""
        cache_key = f"search_log_{timezone.now().strftime('%Y%m%d')}"
        searches = cache.get(cache_key, [])
        searches.append({
            'query': query,
            'user_id': user.id if user else None,
            'timestamp': timezone.now().isoformat(),
            'results_count': results_count
        })
        cache.set(cache_key, searches, 86400)  # 24 hours
    
    @staticmethod
    def get_popular_searches(days=7, limit=10):
        """Get most popular search queries"""
        all_searches = []
        for i in range(days):
            date = (timezone.now() - timedelta(days=i)).strftime('%Y%m%d')
            cache_key = f"search_log_{date}"
            searches = cache.get(cache_key, [])
            all_searches.extend(searches)
        
        # Count query frequency
        query_counts = {}
        for search in all_searches:
            query = search['query'].lower()
            query_counts[query] = query_counts.get(query, 0) + 1
        
        # Sort by frequency
        popular = sorted(query_counts.items(), key=lambda x: x[1], reverse=True)
        return popular[:limit]


class AdvancedSearchEngine:
    """
    Enterprise-grade search engine with intelligent ranking and filtering
    """
    
    @staticmethod
    def normalize_query(query):
        """Normalize search query"""
        if not query:
            return ""
        # Remove extra spaces and convert to lowercase
        return ' '.join(query.lower().strip().split())
    
    @staticmethod
    def get_search_terms(query):
        """Split query into individual search terms"""
        normalized = AdvancedSearchEngine.normalize_query(query)
        # Split by spaces and filter empty strings
        return [term for term in normalized.split() if term]
    
    @staticmethod
    def fuzzy_match_score(text, query):
        """Calculate fuzzy match score (0-100)"""
        if not text or not query:
            return 0
        
        text = text.lower()
        query = query.lower()
        
        # Exact match
        if query in text:
            if text == query:
                return 100
            elif text.startswith(query):
                return 90
            else:
                return 80
        
        # Partial word matches
        query_words = query.split()
        text_words = text.split()
        matches = sum(1 for qw in query_words if any(qw in tw for tw in text_words))
        
        if matches > 0:
            return int((matches / len(query_words)) * 70)
        
        return 0
    
    @staticmethod
    def search_domains(query, limit=None):
        """Search domains with intelligent ranking"""
        if not query:
            return Domain.objects.annotate(
                topic_count=Count('topics'),
                mcq_count=Count('mcqs')
            ).order_by('name')
        
        terms = AdvancedSearchEngine.get_search_terms(query)
        q_objects = Q()
        
        for term in terms:
            q_objects |= Q(name__icontains=term) | Q(description__icontains=term)
        
        domains = Domain.objects.filter(q_objects).annotate(
            topic_count=Count('topics'),
            mcq_count=Count('mcqs'),
            # Ranking: exact match > starts with > contains
            rank=Case(
                When(name__iexact=query, then=Value(100)),
                When(name__istartswith=query, then=Value(90)),
                When(name__icontains=query, then=Value(80)),
                When(description__icontains=query, then=Value(60)),
                default=Value(50),
                output_field=IntegerField()
            )
        ).order_by('-rank', 'name')
        
        if limit:
            domains = domains[:limit]
        
        return domains
    
    @staticmethod
    def search_topics(query, domain_id=None, limit=None):
        """Search topics with intelligent ranking"""
        topics = Topic.objects.select_related('domain')
        
        if domain_id:
            topics = topics.filter(domain_id=domain_id)
        
        if query:
            terms = AdvancedSearchEngine.get_search_terms(query)
            q_objects = Q()
            
            for term in terms:
                q_objects |= (
                    Q(name__icontains=term) | 
                    Q(description__icontains=term) |
                    Q(domain__name__icontains=term)
                )
            
            topics = topics.filter(q_objects)
        
        topics = topics.annotate(
            subtopic_count=Count('subtopics'),
            mcq_count=Count('mcqs'),
            rank=Case(
                When(name__iexact=query, then=Value(100)),
                When(name__istartswith=query, then=Value(90)),
                When(name__icontains=query, then=Value(80)),
                When(description__icontains=query, then=Value(60)),
                When(domain__name__icontains=query, then=Value(50)),
                default=Value(40),
                output_field=IntegerField()
            )
        ).order_by('-rank', 'name')
        
        if limit:
            topics = topics[:limit]
        
        return topics
    
    @staticmethod
    def search_subtopics(query, topic_id=None, limit=None):
        """Search subtopics with intelligent ranking"""
        subtopics = Subtopic.objects.select_related('topic', 'topic__domain')
        
        if topic_id:
            subtopics = subtopics.filter(topic_id=topic_id)
        
        if query:
            terms = AdvancedSearchEngine.get_search_terms(query)
            q_objects = Q()
            
            for term in terms:
                q_objects |= (
                    Q(name__icontains=term) | 
                    Q(description__icontains=term) |
                    Q(topic__name__icontains=term) |
                    Q(topic__domain__name__icontains=term)
                )
            
            subtopics = subtopics.filter(q_objects)
        
        subtopics = subtopics.annotate(
            mcq_count=Count('mcqs'),
            rank=Case(
                When(name__iexact=query, then=Value(100)),
                When(name__istartswith=query, then=Value(90)),
                When(name__icontains=query, then=Value(80)),
                When(description__icontains=query, then=Value(60)),
                When(topic__name__icontains=query, then=Value(50)),
                default=Value(40),
                output_field=IntegerField()
            )
        ).order_by('-rank', 'name')
        
        if limit:
            subtopics = subtopics[:limit]
        
        return subtopics
    
    @staticmethod
    def search_mcqs(query, filters=None, limit=None):
        """
        Advanced MCQ search with multiple filters
        
        filters = {
            'domain_id': int,
            'topic_id': int,
            'subtopic_id': int,
            'batch_id': int,
            'difficulty': str,
            'tag': str,
            'date_from': date,
            'date_to': date,
        }
        """
        mcqs = MCQ.objects.select_related('domain', 'topic', 'subtopic', 'batch')
        
        # Apply filters
        if filters:
            if filters.get('domain_id'):
                mcqs = mcqs.filter(domain_id=filters['domain_id'])
            if filters.get('topic_id'):
                mcqs = mcqs.filter(topic_id=filters['topic_id'])
            if filters.get('subtopic_id'):
                mcqs = mcqs.filter(subtopic_id=filters['subtopic_id'])
            if filters.get('batch_id'):
                mcqs = mcqs.filter(batch_id=filters['batch_id'])
            if filters.get('difficulty'):
                mcqs = mcqs.filter(difficulty=filters['difficulty'])
            if filters.get('tag'):
                mcqs = mcqs.filter(tag__icontains=filters['tag'])
            if filters.get('date_from'):
                mcqs = mcqs.filter(created_at__gte=filters['date_from'])
            if filters.get('date_to'):
                mcqs = mcqs.filter(created_at__lte=filters['date_to'])
        
        # Apply text search
        if query:
            terms = AdvancedSearchEngine.get_search_terms(query)
            q_objects = Q()
            
            for term in terms:
                q_objects |= (
                    Q(question_text__icontains=term) |
                    Q(option_a__icontains=term) |
                    Q(option_b__icontains=term) |
                    Q(option_c__icontains=term) |
                    Q(option_d__icontains=term) |
                    Q(reason__icontains=term) |
                    Q(tag__icontains=term) |
                    Q(domain__name__icontains=term) |
                    Q(topic__name__icontains=term) |
                    Q(subtopic__name__icontains=term)
                )
            
            mcqs = mcqs.filter(q_objects)
        
        # Intelligent ranking
        mcqs = mcqs.annotate(
            rank=Case(
                When(question_text__icontains=query, then=Value(100)),
                When(tag__iexact=query, then=Value(90)),
                When(option_a__icontains=query, then=Value(80)),
                When(option_b__icontains=query, then=Value(80)),
                When(option_c__icontains=query, then=Value(80)),
                When(option_d__icontains=query, then=Value(80)),
                When(reason__icontains=query, then=Value(70)),
                When(domain__name__icontains=query, then=Value(60)),
                When(topic__name__icontains=query, then=Value(50)),
                When(subtopic__name__icontains=query, then=Value(40)),
                default=Value(30),
                output_field=IntegerField()
            )
        ).order_by('-rank', '-created_at')
        
        if limit:
            mcqs = mcqs[:limit]
        
        return mcqs
    
    @staticmethod
    def search_batches(query, limit=None):
        """Search batches"""
        if not query:
            return Batch.objects.annotate(mcq_count=Count('mcqs')).order_by('name')
        
        terms = AdvancedSearchEngine.get_search_terms(query)
        q_objects = Q()
        
        for term in terms:
            q_objects |= Q(name__icontains=term) | Q(description__icontains=term)
        
        batches = Batch.objects.filter(q_objects).annotate(
            mcq_count=Count('mcqs'),
            rank=Case(
                When(name__iexact=query, then=Value(100)),
                When(name__istartswith=query, then=Value(90)),
                When(name__icontains=query, then=Value(80)),
                When(description__icontains=query, then=Value(60)),
                default=Value(50),
                output_field=IntegerField()
            )
        ).order_by('-rank', 'name')
        
        if limit:
            batches = batches[:limit]
        
        return batches
    
    @staticmethod
    def search_all(query, user=None, filters=None):
        """
        Universal search across all models
        Returns comprehensive results with intelligent ranking
        """
        if not query or len(query.strip()) < 2:
            return {
                'query': query,
                'domains': [],
                'topics': [],
                'subtopics': [],
                'mcqs': [],
                'batches': [],
                'total_results': 0
            }
        
        # Perform searches
        domains = list(AdvancedSearchEngine.search_domains(query, limit=10))
        topics = list(AdvancedSearchEngine.search_topics(query, limit=15))
        subtopics = list(AdvancedSearchEngine.search_subtopics(query, limit=15))
        mcqs = list(AdvancedSearchEngine.search_mcqs(query, filters, limit=50))
        batches = list(AdvancedSearchEngine.search_batches(query, limit=10))
        
        total_results = len(domains) + len(topics) + len(subtopics) + len(mcqs) + len(batches)
        
        # Log search for analytics
        SearchAnalytics.log_search(query, user, total_results)
        
        return {
            'query': query,
            'domains': domains,
            'topics': topics,
            'subtopics': subtopics,
            'mcqs': mcqs,
            'batches': batches,
            'total_results': total_results
        }
    
    @staticmethod
    def get_suggestions(query, limit=10):
        """
        Get search suggestions based on partial query
        Returns list of suggested search terms
        """
        if not query or len(query) < 2:
            # Return popular searches if no query
            popular = SearchAnalytics.get_popular_searches(limit=limit)
            return [{'text': q, 'count': c} for q, c in popular]
        
        suggestions = []
        
        # Get suggestions from domains
        domains = Domain.objects.filter(name__icontains=query).values_list('name', flat=True)[:5]
        suggestions.extend([{'text': d, 'type': 'domain'} for d in domains])
        
        # Get suggestions from topics
        topics = Topic.objects.filter(name__icontains=query).values_list('name', flat=True)[:5]
        suggestions.extend([{'text': t, 'type': 'topic'} for t in topics])
        
        # Get suggestions from tags
        tags = MCQ.objects.filter(tag__icontains=query).values_list('tag', flat=True).distinct()[:5]
        suggestions.extend([{'text': t, 'type': 'tag'} for t in tags if t])
        
        return suggestions[:limit]
