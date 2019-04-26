from django.contrib.auth.views import LogoutView
from django.urls import include, path

from main.views import HomeView


urlpatterns = [
    path('', HomeView.as_view()),
    path('accounts/logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
