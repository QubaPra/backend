# backend/tasks/models.py
from django.db import models
from users.models import User
from trials.models import Trial

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    font_color = models.CharField(max_length=50)
    bg_color = models.CharField(max_length=50)
    dark_font_color = models.CharField(max_length=50)
    dark_bg_color = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE, related_name='tasks')
    content = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    end_date = models.CharField(max_length=7, blank=True)  # Format: MM-YYYY
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')
