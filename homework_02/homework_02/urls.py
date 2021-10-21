from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1', include('alexander_yordanov_01.urls')),
]
