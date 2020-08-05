from django.shortcuts import render
from loginapp.models import UserInfo
from django.contrib.auth.decorators import login_required 
def home(request):
    return(render(request,'loginapp/index.html'))
def tester(request):
    return(render(request,'loginapp/testerlogin.html'))
def dev(request):
    return(render(request,'loginapp/devlogin.html'))
def techexpert(request):
    return(render(request,'loginapp/expertlogin.html'))
def projecthead(request):
    return(render(request,'loginapp/projectheadlogin.html'))
def superadmin(request):
    return(render(request,'loginapp/superlogin.html'))

# @login_required(login_url="/")
def verifyTester(request):
    username = request.POST["username"]
    password = request.POST["password"]
    usertype = request.POST["usertype"]
    users = UserInfo.objects.all() 
    for user in users :
        if user.username == username and user.password == password and user.usertype == usertype and username.endswith('@test'):
            return(render(request,'loginapp/tester_page.html',{'testerID':username}))
    return(render(request,'loginapp/invalid.html'))

# @login_required(login_url="/devlogin")
def verifyDev(request):
    username = request.POST["username"]
    password = request.POST["password"]
    usertype = request.POST["usertype"]
    users = UserInfo.objects.all() 
    for user in users :
        if user.username == username and user.password == password and user.usertype == usertype and username.endswith('@dev'):
            return(render(request,'loginapp/dev_page.html',{'devID':username}))
    return(render(request,'loginapp/invalid.html')) 

def verifyExpert(request):
    username = request.POST["username"]
    password = request.POST["password"]
    usertype = request.POST["usertype"]
    users = UserInfo.objects.all() 
    for user in users :
        if user.username == username and user.password == password and user.usertype == usertype and username.endswith('@exp'):
            return(render(request,'loginapp/expert_page.html',{'expertID':username}))
    return(render(request,'loginapp/invalid.html'))
def verifyProhead(request):
    username = request.POST["username"]
    password = request.POST["password"]
    usertype = request.POST["usertype"]
    users = UserInfo.objects.all() 
    for user in users :
        if user.username == username and user.password == password and user.usertype == usertype and username.endswith('@head'):
            return(render(request,'loginapp/prohead_page.html',{'proheadID':username}))
    return(render(request,'loginapp/invalid.html'))    
def verifySuper(request):
    username = request.POST["username"]
    password = request.POST["password"]
    usertype = request.POST["usertype"]
    users = UserInfo.objects.all() 
    for user in users :
        if user.username == username and user.password == password and user.usertype == usertype and username.endswith('@admin'):
            return(render(request,'loginapp/super_page.html',{'adminID':username}))
    return(render(request,'loginapp/invalid.html'))


# def reportBug(request):
#     return(render(request,'loginapp/report_bug.html'))