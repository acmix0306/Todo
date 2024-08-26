from django.shortcuts import render, redirect, get_object_or_404

from.models import Todo

# Create your todo/views.py here.


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        text = request.POST.get('todo_item')
        if text:
            Todo.objects.create(text=text)
    return redirect('todo_list')

def delete_todo(request, id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
    return redirect('todo_list')

def update_todo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.completed = not todo.completed
        todo.save()
    return redirect('todo_list')

def index(request):
    return render(request, 'todo/index.html')


