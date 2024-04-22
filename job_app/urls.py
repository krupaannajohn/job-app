from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_job, name='upload'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
]