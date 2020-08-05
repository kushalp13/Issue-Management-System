from django.urls import path, include

from devapp.views import activeBugs
from django.contrib.auth import views as auth_views  
from django.conf.urls import url 
 
urlpatterns = [     url(r'^/activeBugs', activeBugs),                    
                                    
]