
from django.shortcuts import render

def showindex(request):
    return render(request,"index.html")

def w3(request):
    return render(request, "index.html")