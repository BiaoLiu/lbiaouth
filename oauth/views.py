from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from oauth2_provider.decorators import protected_resource

# Create your views here.
from oauth2_provider.views import ProtectedResourceView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from oauth.serializers.stock import StockSerializer


class TestViewSet(ProtectedResourceView,viewsets.ModelViewSet):
    queryset = User.objects.all()

    # serializer_class = StockSerializer

    def list(self, request, *args, **kwargs):
        user= request.user
        return HttpResponse('test')



@protected_resource()
def test1(request):
    return HttpResponse('test1')


def test2(request):
    return HttpResponse('test2')
