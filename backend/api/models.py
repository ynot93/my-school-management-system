from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """Defines attributes of a note"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    
    def __str__(self) -> str:
        return self.title