from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'mailsends', MailSendViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'messages', MessageViewSet)

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
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),

]