from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm, HiddenInput
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from models import Question, Answer, get_questions
from forms import AskForm, AnswerForm

# Create your views here.

def helper_get_paginated_questions(request, query):
    qs = get_questions(query)
    paginator = Paginator(qs, 10)
    page = request.GET.get('page', 1)
    try:
        qs_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        qs_page = paginator.page(1)
    except EmptyPage:
        qs_page = paginator.page(paginator.num_pages)
    return qs_page

def home(request, *args, **kwargs):
    qs = helper_get_paginated_questions(request, "-added_at")
    return render(request, 'list.html', {'questions': qs})

def question(request, *args, **kwargs):
    qid = int(kwargs['id'])
    try:
        q, title, text, answers = get_questions(qid)
        form = AnswerForm()
        form.initial['question'] = q
        form.fields['question'].widget = HiddenInput()
    except Question.DoesNotExist:
        return HttpResponseNotFound('Question %d does not exist' % qid)        
    return render(request, 'answers.html', {'title': title, 'text':text, 'answers':answers, 'url':reverse('answer'), 'form':form})

def popular(request, *args, **kwargs):
    qs = helper_get_paginated_questions(request, "-rating")
    return render(request, 'list.html', {'questions': qs})

def ask(request, *args, **kwargs):
    if request.method == "GET":
        form = AskForm()
    elif request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect(q.get_absolute_url())
    return render(request, "form.html", {'url':request.path, 'form':form})

def answer(request, *args, **kwargs):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            a = form.save()
            return HttpResponseRedirect(a.question.get_absolute_url())
        return render(request, "form.html", {'url':request.path, 'form':form})

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def nf(request, *args, **kwargs):
    return HttpResponseNotFound('Not found')

