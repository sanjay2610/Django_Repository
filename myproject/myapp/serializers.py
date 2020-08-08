from rest_framework import serializers

from .models import Login, Student, Python, Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class PythonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Python
        fields = "__all__"

