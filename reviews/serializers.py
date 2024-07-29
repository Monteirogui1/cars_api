from rest_framework import serializers
from reviews.models import Review
from cars.serializers import CarListSerializer


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    car = CarListSerializer()

    class Meta:
        model = Review
        fields = ['id', 'car', 'stars', 'comment']

    def validate_comment(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('Comentário não deve ser maior do que 300 caracteres.')
        return value
