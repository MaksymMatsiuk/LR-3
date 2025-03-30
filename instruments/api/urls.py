from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from instruments.views import (
    InstrumentListCreateAPIView, 
    InstrumentDetailAPIView, 
    OrderListCreateAPIView, 
    OrderDetailAPIView
)

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for the project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Routes for Instrument model
    path('instruments/', swagger_auto_schema(
        method='get',
        responses={200: "List of instruments"}
    )(InstrumentListCreateAPIView.as_view()), name='instrument-list-create'),
    
    path('instruments/<int:pk>/', swagger_auto_schema(
        method='get',
        responses={200: "Instrument details"}
    )(InstrumentDetailAPIView.as_view()), name='instrument-detail'),

    # Routes for Order model
    path('orders/', swagger_auto_schema(
        method='get',
        responses={200: "List of orders"}
    )(OrderListCreateAPIView.as_view()), name='order-list-create'),
    
    path('orders/<int:pk>/', swagger_auto_schema(
        method='get',
        responses={200: "Order details"}
    )(OrderDetailAPIView.as_view()), name='order-detail'),

    # Swagger URLs
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger\.json$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
