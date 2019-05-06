from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from main import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/follow/', views.FollowView.as_view()),
    path('accounts/unfollow/', views.UnfollowView.as_view()),
    path('accounts/login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/signup/', views.SignupView.as_view(), name='signup'),
    path('accounts/profile/<slug:username>/', views.ProfileView.as_view(), name='profile'),
    path('downtowns/<int:dtname>', views.DowntownView.as_view(), name='downtowns'),
    path('sell/', views.SellView.as_view(), name='sell'),
    path('close/', views.CloseTicketView.as_view(), name='close'),
    path('attend/', views.AttendView.as_view(), name='attend'),
    path('unattend/', views.UnattendView.as_view(), name='unattend'),
]
