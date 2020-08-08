from django.shortcuts import render
from rest_framework import viewsets
from .serializers import photographySerializer
from .models import photography
from . import models, serializers

# Create your views here.
class photographyViewSet(viewsets.ModelViewSet):
    queryset = photography.objects.all()
    serializer_class = photographySerializer

# class LoginList(APIView):
#     def get(self.request):
#         values = Login.objects.all()
#         Serializers

# class LoginViewSet(viewsets.ModelViewSet)
