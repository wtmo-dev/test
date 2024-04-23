import time
from django.shortcuts import render
from django.http import HttpResponse
from polls.tasks import ppp
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, APIView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class aaas(viewsets.ModelViewSet):

    def list(self):
        print("123456789")
        ppp.delay()
        print("123456789")
        return Response("sssssssss")
    
class aaa(APIView):

    def get(self, request):
        print(request,"request")
        print("1234567890")
        time.sleep(1)
        a= ppp.delay()
        result = a.wait(timeout=None, interval=0.5)
        print(a,"aaaa")
        print(result,"resultresult")
        print("123456789")
        return Response("sssssssss")