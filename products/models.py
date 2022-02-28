from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator

from polymorphic.models import PolymorphicModel


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(PolymorphicModel):
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.01'), message="Price cannot be lower than 0")])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def purchase(self):
        self.quantity -= 1
        self.save()


class Book(Product):
    author = models.CharField(max_length=254, null=True, blank=True)
    release_date = models.CharField(max_length=254, null=True, blank=True)
    signed_copy = models.CharField(max_length=254, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)


class BoxedSet(Product):
    release_date = models.CharField(max_length=254, null=True, blank=True)
    signed_copy = models.CharField(max_length=254, null=True, blank=True)
    details = models.TextField(null=True, blank=True)


class Collectible(Product):
    release_date = models.CharField(max_length=254, null=True, blank=True)
    dimensions = models.CharField(max_length=254, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
