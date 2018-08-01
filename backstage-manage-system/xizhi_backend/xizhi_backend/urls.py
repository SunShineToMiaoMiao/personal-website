"""xizhi_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from learn_django import views as learn_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', learn_views.index, name='home'),
    # path('add/', learn_views.add_technical_tag, name='add'),
    path('add2/<str:tagName>/<str:bgColor>/', learn_views.add_technical_tag_2, name='add2'),
    path('add3/<int:a>/<int:b>/', learn_views.add2, name='add3'),
    path('add4/<int:a>/<int:b>/', learn_views.add3, name='add4'),
    path('demoOne/',learn_views.display_one, name='demoOne'),
]
