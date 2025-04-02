from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterUserView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
