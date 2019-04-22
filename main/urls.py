from django.urls import include, path

from main.views import HomeView


urlpatterns = [
    path('', HomeView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
]
