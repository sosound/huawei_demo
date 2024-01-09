import re
import os
import mimetypes

from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from wsgiref.util import FileWrapper

from .forms import LoginForm
from .functions import robot_push

# Create your views here.


def temp(request):
    result = User.objects.filter(username='xxx')
    # result = result.password
    url = settings.MY_ROBOT
    message = 'success'
    # robot_push(url, message)
    return render(request, 'videojs.html')


def register(request):
    # User.objects.create(username='star', password='www')
    User.objects.create_user(username='star_user1', password='www', email='xxx@qq.com')
    # User.objects.create_superuser(username='star_superuser', password='www')
    return HttpResponse('add user success')


# @login_required
def index(request):
    return render(request, 'index.html')


def show(request):
    result = {
        'code': 0,
        'message': 'success',
        'data': []
    }
    return render(request, 'show.html')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            if authenticate(username=username, password=password):
                login(request, user)
                return redirect('index_name')
            else:
                return HttpResponse('authenticate failed')
        else:
            return HttpResponse('user none')
    else:
        user_all = User.objects.all()
        context = {
            'left': '',
            'right': user_all
        }
        return render(request, 'login.html', context)
