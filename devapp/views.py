from django.shortcuts import render
from testerapp.models import BugInfo
# Create your views here.
def activeBugs(request):
    allbug = BugInfo.objects.all()
    return(render(request,'devapp/activeBugs.html',{'allbug':allbug}))