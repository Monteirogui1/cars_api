from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='cars')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, related_name='cars')
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    plate = models.CharField(max_length=8)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    resume = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.brand.brand} - {self.model} - ({self.year})"
