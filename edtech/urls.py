
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# Swagger and ReDoc imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Shule API",
      default_version='v1',
      description="API documentation for the Shule project",
      contact=openapi.Contact(email="support@shule.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# edtech/urls.py

urlpatterns = [
    path('', include('core.urls')),
    path("admin/", admin.site.urls),
    path('api/', include('study.urls')),


    # Swagger & ReDoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/schema/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



