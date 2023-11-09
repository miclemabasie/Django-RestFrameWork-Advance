from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("<int:api_id>/", views.api_home, name="api_home"),
    path("post/", views.api_post, name="api_post"),
    path("product/", views.product_detail_view, name="product_detial"),
]
