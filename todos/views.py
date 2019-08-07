from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def index(request):
    return render(request, 'index.html')

# Create your views here.
def show_todos(request):
    results = Item.objects.all()
    
    # db['Item'].find({done:true}) <-- MongoDB 
    # results = Item.objects.filter(done=True)
    return render(request, "todo.html", {
        'items' : results
    })
    
    # IF we are using Flask...
    #return render('todo.html', items=results)
    
def create_todo(request):
    if request.method == 'POST':
        # process the form
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(show_todos)
        pass
    
    else:
        form = ItemForm()
        return render(request, "todo_form.html",{
            'form':form
        })
        
def edit_todo(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect(show_todos)
    else:
        form = ItemForm(instance=item)
        return render(request, 'todo_form.html',{
            'form':form
        })
        
