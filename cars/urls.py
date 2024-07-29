from django.conf.urls.static import static
from django.urls import path

from cars.views import CarCreateListView, BrandCreateListView, CarRetrieveUpdateDestroyView, \
    BrandRetrieveUpdateDestroyView, CarStatsView
from core import settings

app_name = 'cars'

urlpatterns = [
    path('cars/', CarCreateListView.as_view(), name='Cars'),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='Cars-Detail-View'),


    path('brand/', BrandCreateListView.as_view(), name='Brand'),
    path('brand/<int:pk>/', BrandRetrieveUpdateDestroyView.as_view(), name='Brand-Detail-View'),

    path('type/', BrandCreateListView.as_view(), name='Type'),
    path('type/<int:pk>/', BrandRetrieveUpdateDestroyView.as_view(), name='Type-Detail-View'),

    path('cars/stats', CarStatsView.as_view(), name='Car-Stats-View'),
]
