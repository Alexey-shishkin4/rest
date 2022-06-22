from django.contrib import admin
from menu.models import Category, Dish, Gallery, Images, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'weight', 'price', 'img_tmb',)
    list_display_links = ('name', )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('item', 'img_tmb', )
    list_display_links = ('item', )


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('img_tmb',)
    list_display_links = ('img_tmb', )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'img_tmb',)
    list_display_links = ('title',)
