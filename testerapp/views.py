from django.shortcuts import render
from .models import BugInfo

# Create your views here.
def reportBug(request):
    return(render(request,'loginapp/report_bug.html'))
def fixedBug(request):
    appName = request.POST["username"]
    password = request.POST["password"]
    usertype = request.POST["usertype"]
    return(render(request,'loginapp/fixed_bug.html'))
def addBugInfo(request):
    appName = request.POST["application_name"]
    moduleName = request.POST["modulename"]
    bugID = appName + "@" + moduleName
    bugDesc = request.POST["debug_info"]
    currBuild = request.POST["current_build"]
    dateRaised = request.POST["dateRaised"]
    detectedBy = request.POST["testerID"]
    bugPriority = request.POST["bug_severity"]
    bugInfo = BugInfo( bugId=appName + "@" + moduleName , bugDesc=bugDesc , bugStatus="ACTIVE" , currBuild=currBuild , dateRaised=dateRaised , appName=appName , detectedBy=detectedBy , bugPriority=bugPriority )
    bugInfo.save()
    return(render(request,'testerapp/reportedBug.html',{'bugID':bugID}))

def viewBug(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'testerapp/viewBug.html',{'allbug':allbug}))

def fixedBug(request): 
       allbug = BugInfo.objects.all()
       return(render(request,'testerapp/fixedBug.html',{'allbug':allbug}))