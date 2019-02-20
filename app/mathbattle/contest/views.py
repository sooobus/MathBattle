from django.shortcuts import render
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from contest_page.models import Contest

@login_required(login_url='../auth/login/')
def contest(request):
    contests = Contest.objects.all()
    hrefs = []
    for i in range(1, len(contests) + 1):
        hrefs.append(i)
    return render(request,'contest/index.html', context={'num_contest': hrefs})
