import datetime
import time
import uuid

import operator
from django.views.generic import TemplateView
from django.core.cache import cache
from rest_framework import status

import article
from .serializers import ConnectedDeviceSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from setuptools._entry_points import render
from django.shortcuts import render
from .models import Group, Student, AccessPending
from .serializers import GroupSerializer, StudentSerializer
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import threading
from django.core.files.base import ContentFile
from django.conf import settings
import qrcode
import datetime

answer = 2
answer1 = 0
isAuthenticated = True
checkTiming = "pending"

class GoshaAnswer(APIView):
    def goshaOne(self, answer=answer, answer1=answer1):
        answer1 += 1
        return answer1

    def goshaReturn(self, answer1 = answer1, answer=answer):
        answer -= answer1
        return answer

    def answer1ReturntoZero(self):
        article.views.answer1 = 0



goshaAnswer = GoshaAnswer()

coolResponse = goshaAnswer.goshaReturn()


class OneAuthorView(APIView):
    def get(self, request, pk):
        student = get_object_or_404(Student.objects.all(), pk=pk)
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
    def post(self, request):
        serializer = ConnectedDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, dname):
        print(dname)
        while (1):
            deviceName = AccessPending.objects.order_by('-connected_at').first()
            serializer = ConnectedDeviceSerializer(deviceName, many=False)
                #if request.user.is_authenticated:
                #if(isAuthenticated == True):
            if (deviceName.status == 'allowed'):
                print('here')
                article.views.coolResponse = goshaAnswer.goshaOne()
                return HttpResponse(1)
            # return Response({'DeviceName': serializer.data})
            else:
                print(deviceName.status)
                time.sleep(1)

    def put(self, request, dname):
        print('good')
        status_saved = AccessPending.objects.order_by('-connected_at').first()
        serializer = ConnectedDeviceSerializer(instance=status_saved, data={'status': "allowed"}, partial=True)

        if (serializer.is_valid()):
            status_saved = serializer.save()
            print(serializer.data)

        return Response({"success": "status '{}' updated successfully".format(status_saved.status)})


class SecondGetDeviceName(APIView):
    def get(self, request):
        print('good')
        status_saved = AccessPending.objects.order_by('-connected_at').first()
        serializer = ConnectedDeviceSerializer(instance=status_saved, data={'status': "allowed"}, partial=True)

        if (serializer.is_valid()):
            status_saved = serializer.save()
            print(serializer.data)

        return Response({"success": "status '{}' updated successfully".format(status_saved.status)})



class GoshaRespone(APIView):
    def get(self, requset):
        print("otvetil")
        return HttpResponse(coolResponse)


def index(request):
    return render(request, 'AfterLoginPAge.html')


def index2(request):
    return render(request, 'index.html')


def camera(request):
    return render(request, 'camera.html')


def anotherCamera(request):
    return render(request, 'qrScanTest3.html')


def authCheck(request):
    username = None
    userID = None
    if request.user.is_authenticated:
        # userID = request.user.user_permissions
        username = request.user.username
        userUUID = uuid.uuid4()
        currentTime = datetime.datetime.now()

    return HttpResponse(userUUID)


class SendTime(APIView):
    def get(self, request):
        article.views.checkTiming = "pending"
        article.views.answer1 = 0
        article.views.answer = 2
        article.views.coolResponse = goshaAnswer.goshaReturn()
        now = datetime.datetime.now()
        return HttpResponse(now)


class CheckingTiming(APIView):
    def get(self, request):
        article.views.checkTiming = request

