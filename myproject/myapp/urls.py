from django.contrib import admin
from django.urls import path, include
from .views import HomePage, LoginViewSet, StudentViewSet, PythonViewSet, RegisterViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'LoginAPI',LoginViewSet)
router.register(r'StudentAPI', StudentViewSet)
router.register(r'PythonAPI', PythonViewSet)
router.register(r'RegisterAPI', RegisterViewSet)

urlpatterns = [
    path('', HomePage, name='home_page'),
    path('api/', include(router.urls), name='api_page'),
]