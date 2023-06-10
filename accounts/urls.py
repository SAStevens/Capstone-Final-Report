from django.urls import path
from .views import SignUpView
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
