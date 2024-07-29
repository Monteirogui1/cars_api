from django.db.models import Avg
from rest_framework import serializers
from cars.models import Car, Brand, Type


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    type = TypeSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'model', 'brand', 'type', 'year', 'color', 'plate', 'price', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

    def validated_resume(self, value):
        if len(value) > 250:
            raise serializers.ValidationError('Resumo não deve ser maior do que 250 caracteres.')
        return value


class CarStatsSerializer(serializers.Serializer):
    total_cars = serializers.IntegerField()
    cars_by_brand = serializers.ListField()
    cars_by_types = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
