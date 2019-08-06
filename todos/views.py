from django.shortcuts import render, HttpResponse

# Create your views here.
def show_todos(request):
    return HttpResponse("Hello World")