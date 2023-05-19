
from django.contrib import admin
from django.urls import path, include


from article import views
from article.views import index, GetDeviceName, SendTime, SecondGetDeviceName, GoshaRespone

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('article.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/loginPage/', index, name='loginPage'),
    path('', views.index2, name='index'),
    path('camera/', views.camera, name='camera'),
    path('add_device/', GetDeviceName.as_view()),
    path('add_device/add_device', SecondGetDeviceName.as_view()),
    path('add_device/<str:dname>', GetDeviceName.as_view()),
    path('sendData/', SendTime.as_view()),
    path('sendAnotherData/', GoshaRespone.as_view())
]
