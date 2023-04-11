from django.contrib import admin

from surur.models import Category, Tour


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'image'
    ]


@admin.register(Tour)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'image1',
        'image2',
        'image3',
        'image4',
        'views',
        'price',
    ]
