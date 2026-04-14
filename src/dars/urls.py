
from django.urls import path
from . import views

urlpatterns = [
    path("univer/", views.UniversitetApiView.as_view()),
    path("teacher/", views.TeacherApiView.as_view()),
    path("group/", views.GroupApiView.as_view()),
    path("student/", views.StudentApiView.as_view()),
]
# api/univer/