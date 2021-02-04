from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from core.views import Test_view

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('', Test_view.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
