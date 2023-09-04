from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('records/<str:username>', views.records, name='records'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('addService', views.addService, name='addService'),
    path('editService/<str:username>/<str:id>', views.editService, name='editService'),
    path('deleteService/<str:id>', views.deleteService, name='deleteService'),
]
