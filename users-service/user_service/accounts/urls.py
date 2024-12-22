from django.urls import path
from .views import RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
]
