from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
  return HttpResponse('Hello World')

def front(request):
    context = {}
    return render(request, "index.html", context)
