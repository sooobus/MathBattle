from django.shortcuts import render
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required


@login_required(login_url='../auth/login/')
def contest(request):
    num = random.randint(1,5)
    num_contest = range(num)
    return render(request,'contest/index.html', context={'num_contest': num_contest})
