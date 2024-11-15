from django.urls import path
from .views import IntegratedJobsView

urlpatterns = [
    path('api/', IntegratedJobsView.as_view(), name='integrated_jobs'),
]
