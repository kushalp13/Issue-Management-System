from django.urls import path, include

from loginapp.views import home, tester, dev, techexpert , projecthead , superadmin , verifyTester , verifyDev , verifyProhead , verifyExpert , verifySuper   
from django.contrib.auth import views as auth_views  
from django.conf.urls import url 
 
urlpatterns = [    url(r'^/$', home),   
                    url(r'^/tester/$', tester),       
                    url(r'^/dev/$', dev),       
                    url(r'^/techexpert/$', techexpert),       
                    url(r'^/projecthead/$', projecthead),
                    url(r'^/superadmin/$', superadmin),
                    url(r'^/verifyTester', verifyTester),
                    url(r'^/verifyDev', verifyDev),
                    url(r'^/verifyProhead', verifyProhead),
                    url(r'^/verifyExpert', verifyExpert),
                    url(r'^/verifySuper', verifySuper),
                                    
] 
 
 
# urlpatterns = [
#     path('',views.home,name='home'),
#     path('tester',views.tester,name='tester'),
#     path('dev',views.dev,name='dev'),
#     path('techexpert',views.techexpert,name='techexpert'),
#     path('projecthead',views.projecthead,name='projecthead'),
#     path('superadmin',views.superadmin,name='superadmin'),
#     path('verifyTester',views.verifyTester,name='verifyTester'),
#     path('verifyDev',views.verifyDev,name='verifyDev'),
#     path('verifyExpert',views.verifyExpert,name='verifyExpert'),
#     path('verifyProhead',views.verifyProhead,name='verifyProhead'),
#     path('verifySuper',views.verifySuper,name='verifySuper'),
#     # path('reportBug',views.reportBug,name='reportBug'),
    
# ]
