from django.shortcuts import get_object_or_404, render

from .models import Category, Item

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category = item.category, is_sold= False).exclude(pk=pk)[0:3]
    data = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'item/detail.html', context=data)