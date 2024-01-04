from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.


def show(request):
    result = {
        'code': 0,
        'message': 'success',
        'data': []
    }
    return render(request, 'show.html')
