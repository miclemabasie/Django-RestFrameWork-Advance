
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include("api.urls")),
    path('api/products/', include("products.urls")),
    path('admin/', admin.site.urls),
    
]
