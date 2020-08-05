from django.shortcuts import render
from testerapp.models import BugInfo
# Create your views here.
def app1_bugs(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'proheadapp/app1_bugs.html',{'allbug':allbug}))

def app2_bugs(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'proheadapp/app2_bugs.html',{'allbug':allbug}))

def app3_bugs(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'proheadapp/app3_bugs.html',{'allbug':allbug}))

def app4_bugs(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'proheadapp/app4_bugs.html',{'allbug':allbug}))