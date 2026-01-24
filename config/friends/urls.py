from django.urls import path
from .views import FriendListView

urlpatterns = [
    path("friend-list/", FriendListView.as_view(), name="friend-list")
]