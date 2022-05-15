from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_create_api_view),
    # path('list/', views.product_list_api_view),
    path('<int:pk>/update', views.product_update_api_view),
    path('<int:pk>/delete', views.product_delete_api_view),    
    path('<int:pk>/', views.product_detail_api_view),


    # path('', views.product_mixin_api_view),
    # path('<int:pk>/', views.product_mixin_api_view),
    # path('<int:pk>/delete', views.product_mixin_api_view),
    # path('<int:pk>/update', views.product_mixin_api_view),


    # path('alt/', views.product_alt_view),
    # path('alt/<int:pk>/', views.product_alt_view)
]
