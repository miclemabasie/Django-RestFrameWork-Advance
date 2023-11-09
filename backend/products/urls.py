from django.urls import path

from . import views

app_name = "products"


urlpatterns = [
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
    path("", views.ProductListCreateAPIView.as_view(), name="product_create"),
    path(
        "update/<int:pk>/",
        views.ProductUpdateDetailView.as_view(),
        name="product_update",
    ),
    path(
        "delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    # extra url for seperate view
    path("list/", views.ProductListAPIView.as_view(), name="product_list"),
    # Functional views
    path("func/", views.product_alt_view, name="func_alt_view"),
    path("func/<int:pk>/", views.product_alt_view, name="func_alt_view"),
]
