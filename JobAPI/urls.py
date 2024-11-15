from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('linkedin/', include('LinkedIn.urls')),
    path('naukri/', include('naukri.urls')),
    path('glassdoor/', include('glassdoor.urls')),
    path('integrated/', include('IntegratedAPI.urls')),
]
