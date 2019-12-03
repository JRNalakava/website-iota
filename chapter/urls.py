from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='chapter_index'),
    path('register/authenticate/<reg_type>', views.authenticate, name='custom_registration'),
]
