from django.urls import path

from . import views

#Available pages:
#   (ip address)
#   (ip address)/upload
urlpatterns = [
    path('home',views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('', views.login, name = 'login')
]