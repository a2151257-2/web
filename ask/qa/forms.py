#!/usr/bin/env python

from django.forms import ModelForm, HiddenInput
import django.forms as forms
from django.contrib.auth.models import User
from models import Answer, Question

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']
    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q
    
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def save(self):
        u = User.objects.create_user(**self.cleaned_data)
        return u

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
