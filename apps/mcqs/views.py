from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import Domain, Topic, Subtopic, Batch, MCQ


def domain_list(request):
    """Public view - anyone can see domains"""
    domains = Domain.objects.annotate(topic_count=Count('topics')).order_by('name')
    return render(request, 'mcqs/domain_list.html', {'domains': domains})


def topic_list(request, domain_id=None):
    """Public view - anyone can see topics"""
    if domain_id:
        domain = get_object_or_404(Domain, id=domain_id)
        topics = Topic.objects.filter(domain=domain).annotate(subtopic_count=Count('subtopics'))
    else:
        domain = None
        topics = Topic.objects.all().select_related('domain').annotate(subtopic_count=Count('subtopics'))
    
    return render(request, 'mcqs/topic_list.html', {
        'topics': topics,
        'domain': domain
    })


def subtopic_list(request, topic_id=None):
    """Public view - anyone can see subtopics"""
    if topic_id:
        topic = get_object_or_404(Topic, id=topic_id)
        subtopics = Subtopic.objects.filter(topic=topic).select_related('topic__domain')
    else:
        topic = None
        subtopics = Subtopic.objects.all().select_related('topic__domain')
    
    return render(request, 'mcqs/subtopic_list.html', {
        'subtopics': subtopics,
        'topic': topic
    })


@login_required
def mcq_list(request):
    """Protected view - only logged-in users can access"""
    user = request.user
    
    # Check if user has MCQ access
    if not user.has_mcq_access():
        messages.error(request, 'Your account does not have MCQ access. Please contact administrator.')
        return render(request, 'mcqs/access_denied.html')
    
    # Get filter parameters
    domain_id = request.GET.get('domain')
    topic_id = request.GET.get('topic')
    subtopic_id = request.GET.get('subtopic')
    batch_id = request.GET.get('batch')
    difficulty = request.GET.get('difficulty')
    tag = request.GET.get('tag')
    keyword = request.GET.get('keyword')
    
    # Base queryset with optimizations
    mcqs = MCQ.objects.select_related('domain', 'topic', 'subtopic', 'batch').all()
    
    # Apply filters
    if domain_id:
        mcqs = mcqs.filter(domain_id=domain_id)
    if topic_id:
        mcqs = mcqs.filter(topic_id=topic_id)
    if subtopic_id:
        mcqs = mcqs.filter(subtopic_id=subtopic_id)
    if batch_id:
        mcqs = mcqs.filter(batch_id=batch_id)
    if difficulty:
        mcqs = mcqs.filter(difficulty=difficulty)
    if tag:
        mcqs = mcqs.filter(tag__icontains=tag)
    if keyword:
        mcqs = mcqs.filter(
            Q(question_text__icontains=keyword) |
            Q(option_a__icontains=keyword) |
            Q(option_b__icontains=keyword) |
            Q(option_c__icontains=keyword) |
            Q(option_d__icontains=keyword)
        )
    
    # Pagination
    paginator = Paginator(mcqs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get filter options
    domains = Domain.objects.all()
    topics = Topic.objects.all()
    subtopics = Subtopic.objects.all()
    batches = Batch.objects.all()
    
    context = {
        'page_obj': page_obj,
        'domains': domains,
        'topics': topics,
        'subtopics': subtopics,
        'batches': batches,
        'selected_domain': domain_id,
        'selected_topic': topic_id,
        'selected_subtopic': subtopic_id,
        'selected_batch': batch_id,
        'selected_difficulty': difficulty,
        'selected_tag': tag,
        'keyword': keyword,
    }
    
    return render(request, 'mcqs/mcq_list.html', context)


@login_required
def mcq_detail(request, mcq_id):
    """Protected view - only paid users can see MCQ details"""
    user = request.user
    
    # Check if user has MCQ access
    if not user.has_mcq_access():
        messages.error(request, 'Your account does not have MCQ access. Please contact administrator.')
        return render(request, 'mcqs/access_denied.html')
    
    mcq = get_object_or_404(MCQ.objects.select_related('domain', 'topic', 'subtopic', 'batch'), id=mcq_id)
    
    return render(request, 'mcqs/mcq_detail.html', {'mcq': mcq})
