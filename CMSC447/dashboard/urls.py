from django.urls import path

from . import views

#Available pages:
#   (ip address)
#   (ip address)/upload
urlpatterns = [
    path('student',views.student, name='student'),
    path('admin', views.admin, name='admin'),
    path('', views.login, name = 'login')
]