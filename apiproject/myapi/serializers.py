from rest_framework import serializers
from .models import photography

class photographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = photography
        fields = ('id', 'name', 'alias')
        # fields = '__all__'

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Login
#         fields="__all__"

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields="__all__"
        