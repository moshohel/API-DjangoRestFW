from django.contrib import admin
from django.urls import path, include

from core.views import Test_view

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', Test_view.as_view(), name='test')
]
