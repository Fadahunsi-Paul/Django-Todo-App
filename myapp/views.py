from django.shortcuts import render,redirect
from myapp.model.task import Task
from .forms import TodoForm
from django.http import Http404

# Create your views here.
def home(request):
    Tasks = Task.objects.all
    context = {'Tasks':Tasks}
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