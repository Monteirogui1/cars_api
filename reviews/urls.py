from django.conf.urls.static import static
from django.urls import path

from core import settings
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

app_name = 'reviews'

urlpatterns = [
    path('reviews/', ReviewCreateListView.as_view(), name='Reviews'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='Reviews-Detail-View')
]
