# ice_cream/admin.py
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Wrapper, Topping

# ...и регистрируем её в админке:
admin.site.register(Topping)
admin.site.register(Wrapper)

admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'created_at'
    )
    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('is_published', 'created_at')
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )

admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)