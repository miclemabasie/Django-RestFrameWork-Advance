from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("<int:api_id>/", views.api_home, name="api_home"),
]
