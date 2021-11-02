"""homework_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('06/', include('vladislav_kolev_06.urls')),
    path('18/', include('stelian_todorichkov_18.urls')),
    path('13/', include('Martin_Georgiev_13.urls')),
    path('19/', include('teodor_dishanski_19.urls')),
    path('martin_dinev_15/', include('Martin_Dinev_15.urls')),
    path('17/', include('petar_damyanov_17.urls'))
]
