from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings

schema_view = get_schema_view(
    openapi.Info(
        title="INTER IELTS API",
        default_version='v1',
        description="API description",
    ),
    public=True,
    url="https://themeless-constance-zoomorphic.ngrok-free.dev",
    permission_classes=[permissions.IsAuthenticated, ],
)

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

    path("api/experts-part-1/", include("experts.part_1.urls")),
    path("api/experts-part-2/", include("experts.part_2.urls")),
    path("api/experts-part-3/", include("experts.part_3.urls")),
    # path("api/experts-writing/", include("experts.experts_writing.urls")),
    # path("api/experts-speaking/", include("experts.experts_speaking.urls")),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("swagger/", csrf_exempt(schema_view.with_ui("swagger", cache_timeout=0)), name="swagger"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
