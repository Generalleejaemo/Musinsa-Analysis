"""musinsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import index
from main.views import *
 
urlpatterns = [
    path('', index, name="index"),
    path('top10/', top10_html, name="top10_html"),
    path('good_top10/', good_top10_html, name="good_top10_html"),
    path('bad_top10/', bad_top10_html, name="bad_top10_html"),
    path('review/', reviews_html, name="reviews_html"),
    path('predict', predict, name="predict"),
    path('admin/', admin.site.urls),
]
