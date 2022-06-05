
from django.contrib import admin
from django.urls import path,include
from .yasg import urlpatterns as yasg_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('app.urls')),
    path('outer_service/',include('outer.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]


urlpatterns += yasg_patterns
