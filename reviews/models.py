from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cars.models import Car


class Review(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.car
