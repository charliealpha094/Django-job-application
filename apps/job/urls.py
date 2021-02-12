# Done by Carlos Amaral (2021/02/05)

from django.urls import path, include
from .api import api_search
from . import views

urlpatterns = [
    path('api/search/', api_search, name='api_search'),
    path('search/', views.search, name='search'),
    path('add/', views.add_job, name='add_job'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('<int:job_id>/edit/', views.edit_job, name='edit_job'),
    path('<int:job_id>/apply_for_job/', views.apply_for_job, name='apply_for_job')
]
