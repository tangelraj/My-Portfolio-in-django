from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('education/', views.education, name="education"),
    path('experience/', views.experience, name="experience"),
    path('skills/', views.skills, name="skills"),
    path('github/', views.github, name="github"),  # NEW PAGE
]
