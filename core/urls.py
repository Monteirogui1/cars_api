from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls', namespace='authentication')),
    path('api/v1/', include('cars.urls', namespace='cars')),
    path('api/v1/', include('reviews.urls', namespace='reviews')),
]
