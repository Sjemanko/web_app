from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('persons/<int:id>/', views.person_details),
    path('persons/add-person', views.add_person),
    path('persons/', views.person_list),
    path('persons/delete/<int:pk>', views.delete_person),
    path('persons/update/<int:pk>', views.update_person),
    path('teams/<int:id>/', views.team_details),
    path('teams/add-team', views.add_team),
    path('teams/', views.team_list),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('team/<int:id>/members/', views.show_team_members),
    path('perms/', views.check_permissions),
    path('team/<int:pk>/details', views.TeamDetail.as_view())
]
