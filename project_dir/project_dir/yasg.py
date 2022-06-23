from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="RESTful backend service [demo]:  Created By Ivan Goncharov\n\n",
      default_version='0.0.1',
      description=f"<h2>For test operations go to -  http://localhost/redoc/\n\n</h2>"
                  f"This is test/demo project created for Fullstat\n\n"
                  f"Stack of technologies:\n"
                  f"Django (Python)\n"
                  f"Djangorestframework - Restfull backend\n"
                  f"Postgress - database\n"
                  f"Redis - data for Celery\n"
                  f"Celery - distributed task system \n"
                  f"Djoser - JWT authentication \n"
                  f"Swagger/DRF-Yasg - docs API\n\n\n\n\n"
                  f"IMPORTANT - In admin panel[periodic tasks] you should put Positional Arguments:",
      license=openapi.License(name="@EwanPotterman / ivan.stereotekk@gmail.com "),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger_get_file/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]