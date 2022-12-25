
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.data_form, name="data_create"),
    path('data/', views.data_read, name="data_read"),
]
