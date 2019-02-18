from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Task, Solves
from .forms import NumSolveForm
from .сheker import Checker

def task(request, task_id):
    task = Task.objects.last()
    if request.method == "POST":
        form = NumSolveForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            username = request.user.id
            checker = Checker(task_id - 1)
            res = checker.check(answer)
            print(res)
            solve = Solves(username, answer, True)
            solve.save()
        return HttpResponse(render(request, 'contest/task.html', {"text" : task.text, "form" : form}))


    else:
        return HttpResponse(render(request, 'contest/task.html', {"text" : task.text, "form" : NumSolveForm()}))
