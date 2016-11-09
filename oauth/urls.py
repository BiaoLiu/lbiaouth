# coding: utf-8
from django.conf.urls import url, include
from oauth import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', views.TestViewSet)

urlpatterns = [
    url(r'', include(router.urls)),

    url(r'^test1/$', views.test1),

    url(r'^test1/$', views.test2),

]
