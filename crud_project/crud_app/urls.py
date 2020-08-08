from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp, name="create_employee"),
    path('show/',views.show,name="emp_list"),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),

]