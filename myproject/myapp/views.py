from django.shortcuts import render, redirect
from . import models
from .models import Login, Student, Python, Register
from .serializers import LoginSerializer, StudentSerializer, PythonSerializer, RegisterSerializer
from . import forms
from .forms import RegisterForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.
def HomePage(request):
    form  = RegisterForm

    if request.method=='POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            v_email = form.cleaned_data['verify_email']
            text = form.cleaned_data['text']
            password = form.cleaned_data['password']

            new_login = Register()
            new_login.name = name
            new_login.email = email
            new_login.text = text
            new_login.save()

            return HttpResponseRedirect('api/')

    return render(request, 'index.html', {'form': form})

# class LoginList(APIView):
#     def get(self, request):
#         values = Login.objects.all()
#         Serializer = LoginSerializer(values, many=True)
#         return Response(Serializer.data)

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class PythonViewSet(viewsets.ModelViewSet):
    queryset = Python.objects.all()
    serializer_class = PythonSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer