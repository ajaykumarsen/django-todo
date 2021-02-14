from django.shortcuts import render, redirect
from .models import TodoItem
from app.forms import TodoForm

# Create your views here.
def todoView(request):
    form = TodoForm()
    items = TodoItem.objects.all()
    context = { "items": items,
                "form": form }
    return render(request, 'todo.html', context)

def addTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # new_item = TodoItem(content = request.POST['content'])
            new_item = TodoItem(content = form.cleaned_data['content'])
            new_item.save()
            return redirect('home')
        else:
            return redirect('home')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id = todo_id)
    item_to_delete.delete()
    return redirect('home')
