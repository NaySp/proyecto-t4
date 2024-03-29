from django.urls  import path,include,re_path
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from django.urls  import path 
from . import views

urlpatterns = [
    path('', views.login, name='login_redirect'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('chargeAccountForm/', views.createChargeAccountForm, name = "viewChargeAccountForm"),
    path('Ventanilla unica resumida/', views.ventanillaUnicaResumida),
     path('Ventanilla unica/', views.ventanillaUnica),
]

urlpatterns += [ 
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]