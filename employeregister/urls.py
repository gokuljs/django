from django.urls import path, include
from . import views

urlpatterns = [
    path('',)
    path('list/', views.employee_list),
]
