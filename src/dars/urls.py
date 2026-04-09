
from django.urls import path
from . import views

urlpatterns = [
    path('universitet/', views.UniversitetApiView.as_view()),
]
