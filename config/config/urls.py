from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),

    path("api/friends/", include("friends.urls")),
    path("api/ads/", include("ads.urls")),
    path("api/flashcards/", include("flashcards.urls")),
    path("api/followings/", include("followings.urls")),
    path("api/steaks/", include("steaks.urls")),
    path("api/subscriptions/", include("subscriptions.urls")),
    path("api/achievements/", include("achievements.urls")),

    path("api/experts-writing/", include("experts.experts_writing.urls")),
    path("api/experts-speaking/", include("experts.experts_speaking.urls")),

    path("api/candidates-writing/", include("candidates.candidates_writing.urls")),
    path("api/candidates-speaking/", include("candidates.candidates_speaking.urls")),
]