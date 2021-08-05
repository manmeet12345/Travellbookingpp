from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def add(request):
    num1 = request.POST['first_num']
    num2 = request.POST['second_num']
    sum = int(num1)+int(num2) 

    return render(request,"result.html",{'Addition':sum})



def home(request):
    return render(request,"base.html")
    