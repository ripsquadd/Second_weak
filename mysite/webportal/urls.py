from django.urls import path

from .views import index, WPLoginView, profile, WPLogoutView, WPRegisterViews, create, delete

app_name = 'webportal'
urlpatterns = [
    path('', index, name='index'),
    path('accounts/login', WPLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', WPLogoutView.as_view(), name='logout'),
    path('accounts/register/', WPRegisterViews.as_view(), name='register'),
    path('accounts/profile/<pk>', delete, name='delete'),
    path('accounts/create/', create, name='create'),
]