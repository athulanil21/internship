from django.urls import path
from . import views
# from .views import ping_view

app_name = "app_name"

urlpatterns = [

    # path('printfun', views.index, name="index"),
    path('', views.printfun, name="printfun"),
    path('ping/', views.ping_view, name="ping_view"),
    path('ssl/', views.ssl_view, name="ssl_view"),
    path('http_check/', views.check_http_view, name="check_http_view"),
    path('http_ssl/', views.check_ssl_view, name="check_ssl_view"),
    path('checkcm/', views.check_cmtech_view, name="check_cmtech_view"),
    path('check_cloudfare_view/', views.check_cloudfare_view, name="check_cloudfare_view"),
    path('check_ns_view/', views.check_ns_view, name="check_ns_view")


]


