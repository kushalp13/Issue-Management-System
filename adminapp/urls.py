from django.urls import path, include

from adminapp.views import fixedBugs , activeBugs , duplicateBugs
from django.contrib.auth import views as auth_views  
from django.conf.urls import url 
 
urlpatterns = [     url(r'^/activeBugs', activeBugs),
                    url(r'^/duplicateBugs', duplicateBugs),
                    url(r'^/fixedBugs', fixedBugs),
]