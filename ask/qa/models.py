from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name="question_author")
    likes = models.ManyToManyField(User)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    
def get_questions(query):
    if isinstance(query, int):
        q = Question.objects.get(id=query)
        return q.title, q.text, Answer.objects.filter(question = q)
    if query in ("-added_at", "-rating"):
        all_q = Question.objects.order_by(query)
        return all_q
    raise ValueError, query
