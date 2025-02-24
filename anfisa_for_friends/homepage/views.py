from django.shortcuts import render

# from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    # Запрос:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description', 'category__title'
    ).filter(
        # Вернуть только те объекты IceCream, у которых
        # в связанном объекте Category в поле is_published хранится значение True:
        category__is_published=True
    ).filter(
        # Можно через Q-объекты, так еще компактнее.
        # Q(is_published=True) & Q(is_on_main=True)
        is_on_main=True,
        is_published=True,
    ).order_by('title')[1:4]
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, 'homepage/index.html', context)
