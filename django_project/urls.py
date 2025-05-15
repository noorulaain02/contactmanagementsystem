from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, include

from postingapp import views

urlpatterns = [
   # path('',views.login),
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),


    path('add/', views.add),
    path('add/addrecord/', views.addrecord),

    path('show/', views.show, name='show'),
    path('search/', views.search, name='search'),

    path('update/<int:AREA_CD>', views.update, name='update'),
    path('update/updaterecord/<int:AREA_CD>', views.updaterecord, name='updaterecord'),
    path('delete/<int:AREA_CD>', views.delete, name='delete'),
    path('search/delete/<int:AREA_CD>', views.delete, name='delete'),
    path('search/update/<int:AREA_CD>', views.update, name='update'),
    path('search/update/updaterecord/<int:AREA_CD>', views.updaterecord, name='updaterecord'),

]
