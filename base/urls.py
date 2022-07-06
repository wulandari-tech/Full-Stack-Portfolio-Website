from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('project/<slug:slug>/', views.projectPage, name="project"),
    path('add-project/', views.addProject, name="add-project"),
    path('edit-project/<slug:slug>/', views.editProject, name="edit-project"),
    path('post-project/', views.postProjects, name="post-project"),
    path('delete-project/<slug:slug>/', views.deleteProject, name="delete-project"),
    path('send_email/', views.sendEmails, name="send_email"),
    path('add-skill/', views.addSkills, name="add-skill"),
    path('add-endorsement/', views.addEndorsements, name="add-endorsement"),
    path('NoDemo/', views.Nodemo, name="NoDemo"),
   

    
]
 