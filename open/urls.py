"""iota_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/basic', views.basic_register, name='basic_registration'),
    path('about/', TemplateView.as_view(template_name="open/pages/about.html"), name='about'),
    path('rush/', views.rush, name='rush'),
    path('icm/', views.icm, name='icm'),
    path('sponsorship/', TemplateView.as_view(template_name="open/pages/sponsorship.html"), name='sponsorship'),
    path('donations/', TemplateView.as_view(template_name="open/pages/donation.html"), name='donation'),
]
