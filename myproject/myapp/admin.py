from django.contrib import admin
from .models import Register, Login, Student, Python

# Register your models here.
admin.site.register(Register)
admin.site.register(Python)
admin.site.register(Login)
admin.site.register(Student)
