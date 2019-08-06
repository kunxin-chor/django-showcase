from django.shortcuts import render

# Create your views here.
def show_todos(request):
    return HttpResponse("Hello World")