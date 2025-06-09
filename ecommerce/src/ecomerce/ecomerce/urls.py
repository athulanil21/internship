from django.contrib import admin
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("products.urls", namespace="products")),
    # path('', include("base.urls", namespace="base")),

]
