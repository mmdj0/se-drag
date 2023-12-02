from django.urls import path

from . import views

app_name = "chatapp"


urlpatterns = [
    
    path("", views.rooms, name="rooms"),
    path('create/', views.create_room, name='create_room'),
    path("<int:id_room>", views.room, name="room"),
    path('<int:room_id>/update/', views.update_room, name='update_room'),
    path('<int:room_id>/delete/', views.delete_room, name='delete_room'),
    path("group/<int:id>/<int:group_id>/", views.room_group, name="room-group"),   
]
