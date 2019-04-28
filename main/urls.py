from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from main.views import HomeView


urlpatterns = [
    path('', HomeView.as_view()),
    path('accounts/login', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
]
