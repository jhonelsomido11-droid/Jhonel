from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('facts/', views.facts, name='facts'),
    path('checklist/', views.checklist, name='checklist'),
    path('quiz/', views.quiz, name='quiz'),
    path('plan/', views.plan, name='plan'),
]
