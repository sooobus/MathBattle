from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Contest
from django.template import loader
from django.utils.timezone import now
def contest(request, contest_id):
    contest = Contest.objects.all()[contest_id - 1]
    if (contest.dateST < now() and contest.dateED > now()):
        tasks = [contest.task_1_id, contest.task_2_id, contest.task_3_id, contest.task_4_id, contest.task_5_id,
                 contest.task_6_id]
        while (tasks[-1] == -1):
            tasks.pop()
        print(tasks)
        template = loader.get_template('contest/contest_page_start.html')
        return HttpResponse(template.render({"tasks": tasks}, request))
    elif contest.dateST > now() :
        template = loader.get_template('contest/contest_page_notstart.html')
        return HttpResponse(template.render({},request))
    else:
        template = loader.get_template('contest/contest_page_end.html')
        return HttpResponse(template.render({}, request))

