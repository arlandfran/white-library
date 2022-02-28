from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from .models import Category, Product, Book, BoxedSet, Collectible


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ProductChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Product


@admin.register(Book)
class BookAdmin(ProductChildAdmin):
    base_model = Book


@admin.register(BoxedSet)
class BoxedSetAdmin(ProductChildAdmin):
    base_model = BoxedSet


@admin.register(Collectible)
class CollectibleAdmin(ProductChildAdmin):
    base_model = Collectible


@admin.register(Product)
class ProductParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Product
    child_models = (Book, BoxedSet, Collectible)
    list_filter = (PolymorphicChildModelFilter,)
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)
