from django.shortcuts import render
from .models import House
from .filters import HouseFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


# Filter houses
def house_filter(request):
    base_qs = House.objects.all().select_related('community')
    f = HouseFilter(request.GET, queryset=base_qs)
    paginator = Paginator(f.qs, 5)
    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    context = {'page_obj': page_obj, 'paginator': paginator, 'is_paginated': is_paginated, 'filter': f, }

    return render(request, 'house/house_filter.html', context)
