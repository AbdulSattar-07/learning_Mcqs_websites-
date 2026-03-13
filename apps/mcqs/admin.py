from django.contrib import admin
from .models import Domain, Topic, Subtopic, Batch, MCQ


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'domain', 'created_at', 'updated_at']
    list_filter = ['domain']
    search_fields = ['name', 'description', 'domain__name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'created_at', 'updated_at']
    list_filter = ['topic__domain', 'topic']
    search_fields = ['name', 'description', 'topic__name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']


@admin.register(MCQ)
class MCQAdmin(admin.ModelAdmin):
    list_display = ['id', 'domain', 'topic', 'subtopic', 'difficulty', 'tag', 'batch', 'created_at']
    list_filter = ['domain', 'topic', 'subtopic', 'difficulty', 'batch']
    search_fields = ['question_text', 'tag', 'domain__name', 'topic__name', 'subtopic__name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Classification', {
            'fields': ('domain', 'topic', 'subtopic', 'batch', 'difficulty', 'tag')
        }),
        ('Question', {
            'fields': ('question_text',)
        }),
        ('Options', {
            'fields': ('option_a', 'option_b', 'option_c', 'option_d')
        }),
        ('Answer', {
            'fields': ('correct_answer', 'reason')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
