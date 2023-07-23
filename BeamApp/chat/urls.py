from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('forumpages', views.forum_pages, name='forumpages'),
    path("", views.forum, name="forum"),
    path("discussion/<int:myid>/", views.discussion, name="Discussions"),
    # path('<int:room_id>/', views.chat_room,
    #      name='chat_room'),
    # path('join-room/',
    #         views.JoinRoomView.as_view(),
    #         name='join_room'),
]