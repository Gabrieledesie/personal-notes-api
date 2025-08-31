from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.views.static import serve
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Notes API",
        default_version='v1',
        description="API for managing notes",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@notes.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/notes/', include('notes.urls')),
    path('api/followers/', include('followers.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('favicon.ico', serve, {'document_root': settings.STATIC_ROOT, 'path': 'favicon.ico'}),
]