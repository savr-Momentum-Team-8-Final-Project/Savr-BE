from SAVR.settings import DEBUG
from django.urls import path, include
from trip import views




urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]