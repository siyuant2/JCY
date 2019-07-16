from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('studentList', views.list_students, name='list_students'),
    path('studentList/new', views.create_student, name='create_student'),
    path('studentList/update/<int:id>/', views.update_student, name='update_student'),
    path('studentList/delete/<int:id>/', views.delete_student, name='delete_student'),
]
