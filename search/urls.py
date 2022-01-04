# search/urls.py

from django.urls import path

from .views import homeView, searchView

urlpatterns = [
    path('search/', searchView.as_view(), name = 'search'),
    path('', homeView.as_view(), name = 'index'),
]