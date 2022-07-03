from django.contrib import admin
from cart.models import Orders

@admin.register(Orders)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'table', 'phone', 'date')
    list_display_links = ('name', )
