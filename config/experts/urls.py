from django.urls import path, include

urlpatterns = [
    path('speaking', include("speaking.urls"), name="speaking"),
]
