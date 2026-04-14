
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("dars.urls")),
    path('api2/', include("dars2.urls")),
]
