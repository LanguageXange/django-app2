from django.urls import path
from .views import index, job_detail
urlpatterns = [
    path('', index, name='home'),
    path('job/<int:postId>/', job_detail, name='job-detail')
]