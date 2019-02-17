from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Task
def task(request, task_id):
    task = Task.objects.last()
    print(task.text)
    return HttpResponse(task.text)