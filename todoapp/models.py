from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField(null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    def save(self, *args, **kwargs):
        if self.due_date and self.timestamp and self.timestamp > self.due_date:
            raise ValueError("Due Date cannot be before the Timestamp created.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({', '.join(tag.name for tag in self.tags.all())})"
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name