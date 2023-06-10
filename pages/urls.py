from django.urls import path

from .views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("", AboutPageView.as_view(), name="about"),
    path("", ContactPageView.as_view(), name="contact"),
]
