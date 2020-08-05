from django.urls import path, include

from proheadapp.views import app1_bugs , app2_bugs , app3_bugs , app4_bugs
from django.contrib.auth import views as auth_views  
from django.conf.urls import url 
 
urlpatterns = [     url(r'^/app1_bugs', app1_bugs),
                    url(r'^/app2_bugs', app2_bugs),
                    url(r'^/app3_bugs', app3_bugs),
                    url(r'^/app4_bugs', app4_bugs),

                                    
]