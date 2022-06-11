
from django.contrib import admin
from django.urls import path,include
from .yasg import urlpatterns as yasg_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('app.urls')),
    path('outer_service/',include('outer.urls')),
    path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]


urlpatterns += yasg_patterns
