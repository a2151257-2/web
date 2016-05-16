from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from django.contrib.auth.models import User
from models import Question, Answer, get_questions

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
        title, text, answers = get_questions(qid)
    except Question.DoesNotExist:
        return HttpResponseNotFound('Question %d does not exist' % qid)        
    return render(request, 'answers.html', {'title': title, 'text':text, 'answers':answers})

def popular(request, *args, **kwargs):
    qs = helper_get_paginated_questions(request, "-rating")
    return render(request, 'list.html', {'questions': qs})

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def nf(request, *args, **kwargs):
    return HttpResponseNotFound('Not found')

