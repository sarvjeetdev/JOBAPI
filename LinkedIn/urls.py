from django.urls import path
from .views import JobViewSet

job_list = JobViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('jobs/', job_list, name='job-list'),
]
