from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name="question_author")
    likes = models.ManyToManyField(User)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    
