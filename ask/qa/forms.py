#!/usr/bin/env python

from django.forms import ModelForm, HiddenInput
from models import Answer, Question

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']
    def clean(self):
        self.cleaned_data['author_id'] = 1
    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q
    
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
    def clean(self):
        self.cleaned_data['author_id'] = 1
    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a

