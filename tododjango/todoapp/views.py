from django.shortcuts import render
from .models import TodoListItem 
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect , HttpResponse 

def todoappView(request):
    return render(request, 'mytodo.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all() 
    return render(request, 'mytodo.html',
    {'all_items':all_todo_items}) 

def addTodoView(request):
    x = request.POST['content']
    if(x!=""):
      new_item = TodoListItem(content = x)
      new_item.save() 
    return HttpResponseRedirect(reverse('home'))
    # return render(request, 'todo.html')

def deleteTodoView(request, id):
    y = TodoListItem.objects.get(id= id)
    y.delete()
    return HttpResponseRedirect(reverse('home'))

# for edit

# def edit(request, task_id):
#     # updating the page
#     if request.method=="POST":
#     task = TodoListItem.object.get(id=task_id)
#     title = request.POST.get('title')
#     task.title= title
#     task.save()

#     # rendering the page
#     task = TodoListItem.object.get(id=task_id)
#     context = {'title':task.content}
#     print(context)

#     return render(request, 'edit.html'. context)


def edit(request, id):
    # rendaring page
    obj = TodoListItem.objects.get(id=id)
    mydictionary = {
    "content" : obj.content,
    "id" : obj.id
    }
    return render(request,'edit.html',context=(mydictionary))

def update(request,id):    
    content = request.POST['newcontent']
    x = TodoListItem.objects.get(id=id)
    x.content = content

    x.save()
    
    return HttpResponseRedirect(reverse('home'))

# Create your views here.
