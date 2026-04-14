
from django.urls import path
from . import views

urlpatterns = [
    path("todolist/", views.TodoListApiView.as_view()),
]
# api/univer/