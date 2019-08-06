from django.shortcuts import render, HttpResponse

# Create your views here.
def show_todos(request):
    return render(request, "todo.html")