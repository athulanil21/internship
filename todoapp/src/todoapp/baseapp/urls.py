from django.urls import path
from . import views

app_name = "baseapp"

urlpatterns = [
    path('', views.index, name="home"),
    path('delete/<int:pk>/', views.delete, name="task_delete"),
    path('status/change/<int:pk>/', views.changestatus, name="change_status"),
    path('edit/<int:pk>/', views.edittask, name="edit_task"),
]
