from django.shortcuts import render
from clientapp.models import Client,User
from clientapp.forms import ClientForm,UserForm

# Create your views here.
def displayclientform(request):
    form=ClientForm
    return render(request,'clientapp/addclient.html',{'form':form})


def addclient(request):
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,'clientapp/success.html')
            except:
                return render(request,'clientapp/fail.html')

def displayuserform(request):
    form=UserForm
    return render(request,'clientapp/addclient.html',{'form':form})


def adduser(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,'clientapp/success.html')
            except:
                return render(request,'clientapp/fail.html')


def deleteclient(request,clientId):
    client=Client.objects.get(clientId=clientId)
    client.delete()
    return render(request,'clientapp/success.html')


def deleteuser(request,userId):
    User=User.objects.get(userId=userId)
    User.delete()
    return render(request,'clientapp/success.html')