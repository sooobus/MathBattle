from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contest
from django.template import loader
def contest(request, contest_id):
    contest = Contest.objects.last()
    tasks = [contest.task_1_id, contest.task_2_id, contest.task_3_id, contest.task_4_id, contest.task_5_id, contest.task_6_id]
    while (tasks[-1] == -1):
        tasks.pop()
    print(tasks)

    template = loader.get_template('contest/contest_page.html')

    return HttpResponse(template.render({"tasks" : tasks}, request))