# naukri/urls.py

from django.urls import path, include
from .views import JobListingViewSet

job_list = JobListingViewSet.as_view({'get': 'list'})



urlpatterns = [
    path('jobs/', job_list, name='naukri-list'),
]
