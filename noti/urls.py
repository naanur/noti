from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from main import views

schema_view = get_schema_view(
    openapi.Info(
        title="Noti API",
        default_version='v1',
        description="Noti API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cpnkuro@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('main.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path("", views.index, name="index"),
    # path("login", views.login, name="login"),
    # path("logout", views.logout, name="logout"),
    # path("callback", views.callback, name="callback"),
]
