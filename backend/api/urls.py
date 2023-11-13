from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = "api"

urlpatterns = [
    path("", views.api_home, name="api_home"),
    path("post/", views.api_post, name="api_post"),
    path("product/", views.product_detail_view, name="product_detial"),
    path("obtain-token/", obtain_auth_token, name="obtain_token"),
]
