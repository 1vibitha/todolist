from contextlib import redirect_stderr
from django.shortcuts import render,HttpResponse
from home.models import tasks
def home(request):
    context={'success':False}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=tasks(tasktitle=title,taskdesc=desc)
        ins.save() 
        context={'success':True}
    return render(request,'home.html',context)
def task(request):
    alltask=tasks.objects.all()
    context={'task':alltask}
    return render(request,'task.html',context)
def delete(request,task_id):
    obj=tasks.objects.get(id=task_id)
    obj.delete()
    alltask=tasks.objects.all()
    context={'task':alltask}
    return render(request,'task.html',context)
def update(request,task_id):
    obj=tasks.objects.get(id=task_id)
    context={'success':False}
    if request.method=="POST":
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        obj.tasktitle=title
        obj.taskdesc=desc
        obj.save()
        context={'success':True}
    alltask=tasks.objects.all()
    context={'task':alltask}
    return render(request,'task.html',context)
def doupdate(request,task_id):
    obj=tasks.objects.get(id=task_id)
    context={
        'title':obj.tasktitle,
        'desc':obj.taskdesc,
        'id':obj.id
    }
    return render(request,'update.html',context)
