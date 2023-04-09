import datetime
import time
import uuid

import operator
from django.views.generic import TemplateView
from django.core.cache import cache
from rest_framework import status
from .serializers import ConnectedDeviceSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import  HttpResponse
from setuptools._entry_points import render
from django.shortcuts import render
from .camera import gen, VideoCamera
from .models import Group, Student, AccessPending
from .serializers import GroupSerializer, StudentSerializer
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import threading
from django.core.files.base import ContentFile
from django.conf import settings
import qrcode

class OneAuthorView(APIView):
    def get(self, request, pk):
        student  = get_object_or_404(Student.objects.all(), pk=pk)
        serializer = StudentSerializer(student)
        return Response({"Student": serializer.data})

class ArticleView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response({"Group": serializer.data})

    def post(self, request):
        article = request.data.get('Group')
        serializer = GroupSerializer(data=Group)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Group '{}' created successfully".format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Group.objects.all(), pk=pk)
        data = request.data.get('Group')
        serializer = GroupSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(article_saved.title)
        })

#################################
class GetDeviceName(APIView):
    def  post(self, request):
        serializer = ConnectedDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, dname):
        print(dname)
        while(1):
            deviceName = AccessPending.objects.order_by('-connected_at').first()
            ##print(deviceName.connected_at)
            serializer = ConnectedDeviceSerializer(deviceName, many=False)
            if(deviceName.status =='allowed'):
                print('here')
                return Response({'DeviceName': serializer.data})
            else:
                print(deviceName)
                print('try again')
                time.sleep(1)

    def put(self, request, dname):
        status_saved = get_object_or_404(AccessPending.objects.all(), DeviceName = dname)
        serializer = ConnectedDeviceSerializer(instance=status_saved, data={'status': "allowed"}, partial = True)

        if (serializer.is_valid()):
            status_saved = serializer.save()
            print(serializer.data)

        return Response({"success": "status '{}' updated successfully".format(status_saved.status)})



#####################  СДЕЛАТЬ генерация куара запускала гет, косметика



def index(request):
    return render(request, 'AfterLoginPAge.html')

def index2(request):
    return render(request, 'index.html')


def camera(request):
    ##GetDeviceName.get(request)
    return render(request, 'camera.html')

def anotherCamera(request):
    return render(request, 'qrScanTest3.html')

def authCheck(request):
    username = None
    userID = None
    if request.user.is_authenticated:
        #userID = request.user.user_permissions
        username = request.user.username
        userUUID = uuid.uuid4()
        currentTime = datetime.datetime.now()

        qr_file = 'C:/Users/ivanm/source/repos/web-project-example-master/backend/article/templates/qrcode.png'
        data = ""

        with open(r"userUUID.txt", "r") as file:
            for line in file:
                data += line
        img = qrcode.make(data)
        img.save(qr_file)

    return HttpResponse(userUUID)


def qrGEN(request):
    return render(request, "qrCode.html")



