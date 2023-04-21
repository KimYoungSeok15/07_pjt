from django.urls import path
from movies import views

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>', views.actor_detail),
]
