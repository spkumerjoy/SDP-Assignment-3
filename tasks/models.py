from django.db import models
from categories.models import Category

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    assignDate = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title