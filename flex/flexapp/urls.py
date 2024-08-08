from django.urls import path
from . import views

urlpatterns = [

    path('',views.CustomLogin,name="login"),
    path('logout', views.CustomLogout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('updateLeet/<int:count>',views.UpdateLeet, name="updateLeet"),
]