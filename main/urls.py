from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from main.views import (AttendView, CloseTicketView, DowntownView, FollowView,
                        HomeView, ProfileView, SellView, SignupView, UnattendView, UnfollowView)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/follow/', FollowView.as_view()),
    path('accounts/unfollow/', UnfollowView.as_view()),
    path('accounts/login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/profile/<slug:username>/', ProfileView.as_view(), name='profile'),
    path('downtowns/<int:dtname>', DowntownView.as_view(), name='downtowns'),
    path('sell/', SellView.as_view(), name='sell'),
    path('close/', CloseTicketView.as_view(), name='close'),
    path('attend/', AttendView.as_view(), name='attend'),
    path('unattend/', UnattendView.as_view(), name='unattend'),
]
