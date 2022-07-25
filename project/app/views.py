from django.shortcuts import render
from django.views.generic import View






def index(request):
   return render(request,'index.html')

def index2(request):
   return render(request,'index2.html')

def index3(request):
   return render(request,'index3.html')


def emp(request):
    return render(request,'emp.html')
   
def empproduct(request):
    return render(request,'empproduct.html')
   
def product(request):
    return render(request,'product.html')
   
def addproduct(request):
    return render(request,'addproduct.html')

def editproduct(request):
    return render(request,'editproduct.html')

def productreport(request):
    return render(request,'productreport.html')

def empreport(request):
    return render(request,'empreport.html')

def emphome(request):
    return render(request,'emphome.html')

def role(request):
    return render(request,'role.html')

def rolelist(request):
    return render(request,'rolelist.html')  

def sign(request):
    return render(request,'sign-in.html')  

def forget(request):
    return render(request,'forgetpassword.html')



