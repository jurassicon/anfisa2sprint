from django.shortcuts import get_object_or_404, render

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    ice_cream = get_object_or_404(
        IceCream.objects.values(
            'title',
            'description'
        ).filter(is_published=True),
        pk=pk,
    )
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, 'ice_cream/detail.html', context)


def ice_cream_list(request):
    # get_list_or_404() Получаем список объектов.
    context = {}
    return render(request, 'ice_cream/list.html', context)
