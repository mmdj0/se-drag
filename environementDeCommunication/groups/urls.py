from django.urls import path
from . import views
from .views import GroupChatView

app_name = "groups"


urlpatterns = [
    path('group_details/<int:group_id>/', views.details_group, name='group_detail'),
    path('create_group/', views.create_group , name='create_group'),    
    path('group_list/', views.groups_list, name='group_list'), 
    path('update_group/<int:group_id>/', views.update_group, name='update_group'),
    path('delete_group/', views.delete_group, name='delete_group'),
    path('group_chats/', views.group_chats, name='group_chats'),
    path('group_chat/<int:group_id>/', GroupChatView.as_view(), name='group_chat'),
     
]
    

