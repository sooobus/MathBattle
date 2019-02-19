from django.shortcuts import render
from django.http import HttpResponse
#from .models import Grouping

def profile_views(request):
        return HttpResponse(render(request,'userprofile/index.html',{"email" : request.user.email, "username" : request.user.username}))
