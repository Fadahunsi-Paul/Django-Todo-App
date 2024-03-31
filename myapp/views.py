from django.shortcuts import render,redirect,get_object_or_404
from myapp.model.task import Task
from .forms import TodoForm
from django.http import Http404

# Create your views here.
def home(request):
    Tasks = Task.objects.all()
    search_input = request.GET.get('search-area') or ''
    if search_input:
        Tasks = Tasks.filter(title__startswith=search_input)
        #To filter using the first letters, use "title_startswith not icontains" 
    context = {'Tasks':Tasks,'search_input':search_input}
    return render(request,'todo/home.html',context)

def todo_details(request,pk):
    try:
        Tasks = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        raise Http404("Task is Unavailable")
    context ={'Tasks':Tasks}
    return render(request,'todo/todo-details.html',context)

def create_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:home')
        TodoForm()
    context = {'form':form}
    return render(request,'todo/create_todo.html',context) 

def update_todo(request,pk):
    todo = Task.objects.get(pk=pk)
    form= TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:home')
        TodoForm()
    context = {'form':form}
    return render(request,'todo/update_todo.html',context)

def delete_todo(request,pk):
    delete = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        delete.delete()
        return redirect('todo:home')
    context={'delete':delete}
    return render(request,'todo/delete_todo.html',context)