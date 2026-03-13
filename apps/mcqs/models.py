from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'domain'
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name


class Topic(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'topic'
        ordering = ['name']
        unique_together = ['domain', 'name']
        indexes = [models.Index(fields=['domain', 'name'])]
    
    def __str__(self):
        return f"{self.domain.name} - {self.name}"


class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subtopics')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'subtopic'
        ordering = ['name']
        unique_together = ['topic', 'name']
        indexes = [models.Index(fields=['topic', 'name'])]
    
    def __str__(self):
        return f"{self.topic.name} - {self.name}"


class Batch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'batch'
        ordering = ['name']
        verbose_name_plural = 'Batches'
    
    def __str__(self):
        return self.name


class MCQ(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    
    ANSWER_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='mcqs')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='mcqs')
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='mcqs')
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True, related_name='mcqs')
    
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Medium')
    tag = models.CharField(max_length=100, blank=True)
    
    question_text = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)
    reason = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'mcq'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['domain', 'topic', 'subtopic']),
            models.Index(fields=['difficulty']),
            models.Index(fields=['tag']),
            models.Index(fields=['batch']),
        ]
        verbose_name = 'MCQ'
        verbose_name_plural = 'MCQs'
    
    def __str__(self):
        return f"{self.domain.name} - {self.topic.name} - Q{self.id}"
