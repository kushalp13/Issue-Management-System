from django.shortcuts import render
from testerapp.models import BugInfo
# Create your views here.
def activeBugs(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'adminapp/activeBugs.html',{'allbug':allbug}))

def duplicateBugs(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'adminapp/duplicateBugs.html',{'allbug':allbug}))

def fixedBugs(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'adminapp/fixedBugs.html',{'allbug':allbug}))