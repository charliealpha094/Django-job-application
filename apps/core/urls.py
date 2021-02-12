# Done by Carlos Amaral (2021/02/04)

from django.urls import path
from . import views
from django.contrib.auth import views as vw

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', vw.LogoutView.as_view(), name='logout'),
    path('login/', vw.LoginView.as_view(template_name='core/login.html'), name='login')
]
