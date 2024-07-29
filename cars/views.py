from django.db.models import Count, Avg
from django.http import JsonResponse
from rest_framework import generics, views, status, response
from rest_framework.permissions import IsAuthenticated

from core.permissions import GlobalDefaultPermission
from cars.models import Car, Brand, Type
from reviews.models import Review
from cars.serializers import CarSerializer, BrandSerializer, TypeSerializer, CarStatsSerializer, CarListSerializer


class BrandCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Brand deletado com sucesso.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class TypeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Type deletado com sucesso.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class CarCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarListSerializer
        return CarSerializer


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarListSerializer
        return CarSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Car deletado com sucesso.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class CarStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Car.objects.all()

    def get(self, request):
        total_cars = self.queryset.count()
        cars_by_brand = self.queryset.values('brand__name').annotate(count=Count('id'))
        cars_by_types = self.queryset.values('type__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_cars': total_cars,
            'cars_by_brand': cars_by_brand,
            'cars_by_types': cars_by_types,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }

        serializer = CarStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
