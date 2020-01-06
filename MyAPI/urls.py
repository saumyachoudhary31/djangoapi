from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('MyAPI',views.ApprovalsView)
urlpatterns = [
   path('api/',include(router.urls)),
   path('forms/',views.ccontact,name='cform'),
   path('status',views.approvereject)
   ]