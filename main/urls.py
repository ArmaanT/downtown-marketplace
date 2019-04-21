from django.urls import path

from main.views import homepage


urlpatterns = [
    path('', homepage)
]
