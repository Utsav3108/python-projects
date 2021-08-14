from django.contrib.auth.models import User
from calc.models import res123
from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
r1 = res123()
def home(request):
    return render(request,'home.html',{'name':"Utsav!!"})

def add(request):
    
    # r1.val1 = int(request.POST['num1'])
    # r1.val2 = int(request.POST['num2'])
    # r1.rs = r1.val1 + r1.val2
    # r1.esr = r1.val1*r1.val2
    f_name = request.POST['First_name']
    l_name = request.POST['Last_name']
    e_name = request.POST['Email']
    p_name = request.POST['Password']
    userr = f_name+l_name
    print("========================================================================================================")
    user = User.objects.create_user(username=userr,email=e_name,first_name=f_name,last_name=l_name,password=p_name)
    print("============================================================================================================")
    user.save()
    print("user created!")
    
    return render(request,'result.html',{'Firstname':f_name,'Last_name':l_name,'Email':e_name,'Password':p_name})



    