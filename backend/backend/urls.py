
from django.contrib import admin
from django.urls import path, include

from article import views
from article.views import index, camera, GetDeviceName

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('article.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/login/loginPage/', livefe, name='live_camera')
    path('accounts/login/loginPage/', index, name='loginPage'),
    path('', views.index2, name='index'),
    path('camera/', views.camera, name='camera'),
    path('anotherCamera/', views.anotherCamera, name='anotherCamera'),
    path('qrCode/', views.qrGEN, name='qrCode'),
    path('authCheck/', views.authCheck, name='authCheck'),
    path('add_device/', GetDeviceName.as_view()),
    path('add_device/<str:dname>', GetDeviceName.as_view()),
]
