from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Task, Solves
from .forms import NumSolveForm
from .сheker import Checker
def task(request, task_id):
    task = Task.objects.all()[task_id - 1]
    res = "You don't submit this task"
    try:
        old_solves = Solves.objects.filter(username=request.user.id, task_id=task_id).all()
        res = "WA"
        for i in old_solves:
            if (i.isRight == True):
                res = "OK"
                break
    except Exception as e: print(str(e))


    if request.method == "POST":
        res = "Something go wrong"
        form = NumSolveForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            username = request.user.id
            checker = Checker(task_id - 1)
            res = checker.check(answer)
            print(task_id)
            if (res == "OK"):
                solve = Solves(username=username, answer=answer, task_id=task_id, isRight=True)
                solve.save()
            else:
                solve = Solves(username=username, answer=answer, task_id=task_id, isRight=False)
                solve.save()
            print('add')

        return HttpResponse(render(request, 'contest/task.html', {"title" : task.title, "text" : task.text, "form" : form, "res" : res}))
    else:
        return HttpResponse(render(request, 'contest/task.html', {"title" : task.title, "text" : task.text, "form" : NumSolveForm(), "res" : res}))
