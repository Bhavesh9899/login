from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def form(request):
    return render(request,"app/form.html")

def InsertData(request):
    username = request.POST['uname']
    email = request.POST['email']
    password = request.POST['pass']
    user = Register.objects.create(username=username,email=email,password=password)
    return redirect('show')

def ShowPage(request):
    data = Register.objects.all()
    return render(request,"app/show.html",{'key1':data})

def EditPage(request,pk):
    data = Register.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':data})

def UpdateData(request,pk):
    udata = Register.objects.get(id=pk)
    udata.username = request.POST['uname'];
    udata.email = request.POST['email'];
    udata.password = request.POST['pass'];
    udata.save()
    return redirect('show')

def DeleteData(request,pk):
    udata = Register.objects.get(id=pk)
    udata.delete()
    return redirect('show')

def loginpage(request):
    return render(request,"app/login.html")

def login(request):
    email = request.POST['email']
    password = request.POST['pass']

    login = Register.objects.get(email=email)
    if login:
        if login.password == password:
            request.session['id'] = login.id
            return render(request,"app/index.html")

        else: 
            msg = "incorret password"
            return render(request,"app/login.html",{'loginmsg':msg})
    else:
        msg = "invalid email"
        return render(request,"app/login.html",{'loginmsg':msg})




    
