from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

def home(request):
    return HttpResponse("Welcome to Personal Notes API")

schema_view = get_schema_view(
    openapi.Info(
        title="Personal Notes API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
