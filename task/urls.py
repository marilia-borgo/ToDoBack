from .views import listartask, addtask
from . import views
from django.urls import path

urlpatterns = [
    path('tasks/', views.listartask, name='tasklist'),
    path('tasks/new_task', views.addtask, name="addtask"),
]