from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    # task_list = Task.objects.filter(user=request.user)
    context = {
        'username': request.user.username,
        # 'semua_task': task_list,
    }
    return render(request, 'show_todolist.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='login/')
def new_create_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Task.objects.create(title=title, description=description,date=datetime.date.today(), user=request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response
    return render(request,'new_create_todolist.html')

@login_required(login_url='login/')
def updatetask(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.is_finished ^= True
    else:
        return redirect('todolist:show_todolist')
    task.save()
    messages.success(request, 'Status task telah berhasil diubah!')
    return redirect('todolist:show_todolist')

@login_required(login_url='login/')
def deletetask(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.delete()
    else:
        return redirect('todolist:show_todolist')

    messages.success(request, 'Task telah berhasil dihapus!')
    return redirect('todolist:show_todolist')

@login_required(login_url="/todolist/login/")
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")

def addtask(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        )
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "title": task.title,
                    "description": task.description,
                    "is_finished": task.is_finished,
                    "date": task.date,
                },
            },
        )