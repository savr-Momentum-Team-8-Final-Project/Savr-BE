from django.urls import path, include
from trip import views




urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.TripList.as_view(), name='trip_list'),
    path('create/', views.TripCreate.as_view(), name='trip_create'),
    path('<int:pk>/', views.TripDetail.as_view(), name='trip_detail'),
    path('<int:pk>/edit/', views.TripUpdate.as_view(), name='trip_update'),
    path('<int:pk>/delete/', views.TripDelete.as_view(), name='trip_delete'),
    path('<int:pk>/cover/', views.TripUploadView.as_view(), name='image_upload'),
]