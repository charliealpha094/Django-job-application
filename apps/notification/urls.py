# Done by Carlos Amaral (2021/02/09)

from django.urls import path

from . import views

urlpatterns = [
    path('', views.notifications, name='notifications'),
]
