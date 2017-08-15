from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    # return HttpResponse('hello world')

    return render(request, 'index.html')


def page_not_found(request):

    return HttpResponse('page not found')
