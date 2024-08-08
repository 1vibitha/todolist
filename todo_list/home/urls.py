from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('update/<int:task_id>', views.update, name='update'),
    path('doupdate/<int:task_id>', views.doupdate, name='doupdate'),

]