from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('real_time_data_frontend.urls')),
    path('', include('routing.urls')),
    path('', include('channel_layer_redis.urls')),
    path('', include('channel_with_database.urls')),
]
