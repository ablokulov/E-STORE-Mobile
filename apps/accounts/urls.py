from django.urls import path
from .views import UserRegisterViews,UserLoginViews,TokenRefreshViews


urlpatterns = [
    path('auth/register/',UserRegisterViews.as_view(),name='register'),
    path('auth/login/',UserLoginViews.as_view(),name='login'),
    path('auth/token/refresh/',TokenRefreshViews.as_view(),name='refresh')
]
