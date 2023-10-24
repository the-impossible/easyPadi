from django.urls import path
from easypadi_app.views import *

app_name = "app"

urlpatterns = [
    path("", LandingPage.as_view(), name="home"),
]
