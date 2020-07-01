from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education')
]