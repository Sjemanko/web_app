from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/<int:id>/', views.person_details),
    path('persons/add-person', views.add_person),
    path('persons/', views.person_list),
]
