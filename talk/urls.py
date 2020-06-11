from django.urls import path
from . import views

urlpatterns = [
    path('demo01/', views.talk_do, name='talk'),
    path('demo02/', views.repeat_do, name='talk'),
    path('demo03/', views.repeat_js, name='talk'),
]
