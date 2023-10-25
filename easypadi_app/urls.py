from django.urls import path
from easypadi_app.views import *

app_name = "app"

urlpatterns = [
    path("", LandingPage.as_view(), name="home"),
    path("about", AboutPage.as_view(), name="about"),
    path("contact", ContactPage.as_view(), name="contact"),
]
