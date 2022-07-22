from django.contrib import admin
from django.urls import path
from nhanvien import views

urlpatterns = [
 
    path('',views.themnhanvien),
    # path('xuly_themnhanvien/',views.xuly_themnhanvien,name="xuly_themnhanvien"),
    # path('xuly_thoat/',views.xuly_thoat,name="xuly_thoat"),
]
