from django.urls import path, include
from trip import views




urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.TripList.as_view(), name='trip_list'),
    path('create/', views.TripCreate.as_view(), name='trip_create'),
    path('<int:pk>/', views.TripDetail.as_view(), name='trip-detail')
]