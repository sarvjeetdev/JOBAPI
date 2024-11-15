from django.urls import path, include
from .views import JobPostViewSet

job_list = JobPostViewSet.as_view({'get': 'list'})



urlpatterns = [
    path('jobs/', job_list, name='glassdoor-list'),
]