from . import views
from django.urls import path, include

app_name = 'Signup'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('addperson/', views.addperson, name = 'addperson'),
    path('changepassword/', views.changepassword, name = 'changepassword'),
    path('updatepassword/', views.updatepassword, name = 'updatepassword'),

    ]
