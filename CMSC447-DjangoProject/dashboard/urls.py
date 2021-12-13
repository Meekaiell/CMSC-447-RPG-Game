from django.urls import path

from . import views

#Available pages:
#   (ip address)
#   (ip address)/upload
urlpatterns = [
    path('',views.home, name='home'),
    path('upload', views.upload, name='upload')
]