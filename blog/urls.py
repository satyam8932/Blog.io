"""blogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from .views import homePage
from .views import blogPage
from .views import aboutPage
from .views import postPage
from .views import categoryPage

urlpatterns = [
    path('home/',homePage),
    path('',homePage),
    path('blog/',blogPage),
    path('about/',aboutPage),
    path('blog/<slug:url>',postPage),
    path('category/<slug:url>',categoryPage),
    
]
