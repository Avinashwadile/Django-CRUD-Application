from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"app\insert.html")

def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    newUser = student.objects.create(fname=fname,lname=lname,email=email,contact=contact)

    return redirect('showpage')

def showPage(request):
    #Select query in django 
    all_data = student.objects.all()
    return render(request,"app\show.html",{'key1':all_data})

#Edit Page View
def editPage(request,pk):   #pk is Primary Key
    #fetching data of perticular id
    get_data = student.objects.get(id=pk)
    return render(request,"app\edit.html",{'key2':get_data})

#Update Data View
def updataData(request,pk):
    udata = student.objects.get(id=pk)
    udata.fname = request.POST['fname']
    udata.lname = request.POST['lname']
    udata.email = request.POST['email']
    udata.contact = request.POST['contact']
    #query for Update
    udata.save()
    #render to showpage
    return redirect('showpage')

#Delete Data View
def deleteData(request,pk):
    udata = student.objects.get(id=pk)
    #Query for delete data
    udata.delete()
    return redirect('showpage')


