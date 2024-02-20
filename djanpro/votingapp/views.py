from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

arr = ['Javascript','Python','Go','Java','Kotlin'
       ,'PHP','C#','Swift','R','Ruby', 'C and C++'
       , 'TypeScript', 'Scala', 'SQL', 'HTML',' CSS','Perl']
glbcnt = dict()


def index(request):
    
    mydic = {
        "arr": arr
    }
    return render(request, 'index.html', context=mydic)


def result(request):
    mydic= {
        'arr' : arr,
        "glbcnt" : glbcnt
    }
    return render(request, 'results.html', context=mydic)
    

def sortd(request):
    global glbcnt
    glbcnt = dict(sorted(glbcnt.items(),key=lambda x:x[1],reverse=True))
    
    mydic= {
        "arr" : arr,
        "glbcnt" : glbcnt
    }
    return render(request, 'results.html', context=mydic)
    

def getquery(request):
    lan = request.GET['languages']

    if lan in glbcnt:
        glbcnt[lan] += 1
    else:
        glbcnt[lan] = 1
    mydic = {
        "arr": arr,
        "glbcnt": glbcnt,
        "submitted" :True
    }
    return render(request, 'index.html', context=mydic)


def reset(request):
    glbcnt.clear()  
    mydic = {
        "reset" : True
    }
    return render(request, 'index.html', context=mydic)



def subvot(request):
    vot = request.GET['subv']
    arr = []
    arr.append(vot)
    mydic = dict()
    
    return render(request, 'index.html', context=mydic)
