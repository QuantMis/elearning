from django.shortcuts import render
from django.http import HttpResponse

from .models import Player, Course

from django.views.generic import ListView


def dashboard(request):
    return render(request, 'index.html', {})

def training(request):
    return render(request, 'training.html', {})

def question(request):
    return render(request, 'question.html', {})

def discussion(request):
    return render(request, 'discussion.html', {})

def result(request):
    return render(request, 'result.html', {})

def selection(request):
    return render(request, 'selection.html', {})

def exam_selection(request):
    return render(request, 'exam_selection.html', {})

def exam_question(request):
    return render(request, 'exam_question.html', {})
