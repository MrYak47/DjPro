from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def subquery (request):
    q= request.GET['query']
    try:
        ans = eval(q)
        mydic = {
            "q": q,
            "ans" : ans,
            "error" : False,
            "result": True
            
        }
        return render(request, 'index.html', context = mydic)
    except :
        
        mydic ={
            "error": True,
            "result": False
            
        }
        return render(request, 'index.html', context=mydic)
    