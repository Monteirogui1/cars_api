from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import GlobalDefaultPermission
from reviews.models import Review
from reviews.serializers import ReviewSerializer, ReviewListSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListSerializer
        return ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListSerializer
        return ReviewSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Review deletado com sucesso.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
