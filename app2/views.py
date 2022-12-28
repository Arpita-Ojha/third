from django.shortcuts import render

# Create your views here.

def htmlone(request):
    return render(request,'htmlone.html')

def htmltwo(request):
    return render(request,'htmltwo.html')