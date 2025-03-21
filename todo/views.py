from django . shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models 
from todo.models import TODOO
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
     username=request.POST.get('username')
     emailid=request.POST.get('email')
     pwd=request.POST.get('pwd')
     print(username,emailid,pwd)

     my_user=User.objects.create_user(username,emailid,pwd)
     my_user.save()
     return redirect('/login')
    return render(request,'signup.html')

def user_login(request):
   if request.method=='POST':
      username=request.POST.get('username')
      pwd=request.POST.get('pwd')
      print(username,pwd)
      user=authenticate(request,username=username,password=pwd)
      if user is not None:
         auth_login(request,user)
         return redirect('todo')
      else:
        messages.error(request, 'Invalid username or password')
        return redirect('/login')
   return render (request,'login.html')


def todo(request):
   if request.method=='POST':
      title=request.POST.get('title')
      print(title)
      last_task = TODOO.objects.filter(user=request.user).order_by('-task_number').first()
      next_number = last_task.task_number + 1 if last_task else 1
      obj = TODOO(title=title,user=request.user, task_number=next_number)
      obj.save()
      return redirect('todo')
   
   todos = TODOO.objects.filter(user=request.user).order_by('-date')
   return render(request,'todo.html', {'todos':todos})

def edit_todo(request, todo_id):
    todo = TODOO.objects.get(id=todo_id, user=request.user)  # Ensure only the owner can edit
    if request.method == 'POST':
        title = request.POST.get('title')
        todo.title = title
        todo.save()
        return redirect('todo')
    return render(request, 'edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = TODOO.objects.get(id=todo_id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo')
    return render(request, 'delete_todo.html', {'todo': todo})