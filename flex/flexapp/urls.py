from django.urls import path
from . import views

urlpatterns = [

    path('',views.CustomLogin,name="login"),
    path('logout', views.CustomLogout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    # path('updateLeet/<int:count>',views.UpdateLeet, name="updateLeet"),
    path('register', views.register, name="register"),
    path('create-project', views.create_project, name="create_project"),
    path('add-certification', views.add_certification, name="add_certification"), 
    path('faculty', views.faculty, name="faculty"),
    path('edit_project', views.edit_project, name="edit_project"),
    path('delete_project/<int:primary_key>', views.delete_project,name="delete_project"),
    path('delete_certification/<int:primary_key>', views.delete_certification, name="delete_certification"),
    path('edit_certification', views.edit_certification, name="edit_certification"),
]
