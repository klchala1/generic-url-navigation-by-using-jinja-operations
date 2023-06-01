from django.shortcuts import render

# Create your views here.

def dhoni(request):
    return render(request,'csk.html')

def virat(request):
    return render(request,'rcb.html')