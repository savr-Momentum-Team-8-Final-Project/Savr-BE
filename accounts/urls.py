from django.urls import path, include
from .views import SignupView, UserAccountView,UserList
from django.conf.urls import url

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('photo/', UserAccountView.as_view(), name='image_upload'),
    path('summary/', UserList.as_view(), name='user_summary'),

]

## signin: http://localhost:8000/auth/token/login
## logout: http://localhost:8000/auth/token/logout