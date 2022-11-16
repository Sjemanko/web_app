from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/<int:id>/', views.person_details),
    path('persons/add-person', views.add_person),
    path('persons/', views.person_list),
    path('persons/delete/<int:pk>', views.update_delete_person),
    path('persons/update/<int:pk>', views.update_delete_person),
    path('teams/<int:id>/', views.team_details),
    path('teams/add-team', views.add_team),
    path('teams/', views.team_list)
]
