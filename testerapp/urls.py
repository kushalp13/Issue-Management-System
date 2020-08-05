from django.urls import path, include

from testerapp.views import reportBug , fixedBug  , addBugInfo , viewBug , fixedBug
from django.contrib.auth import views as auth_views  
from django.conf.urls import url 
 
urlpatterns = [     url(r'^/reportBug', reportBug),
                    url(r'^/fixedBug', fixedBug),
                    url(r'^/addBugInfo', addBugInfo),
                    url(r'^/viewBug', viewBug),
                    url(r'^/fixedBug', fixedBug),                    
                                    
]