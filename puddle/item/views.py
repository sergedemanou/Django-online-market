from django.shortcuts import get_object_or_404, render

from .models import Category, Item

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    categories = Category.objects.all()
    data = {
        'item': item,
        'categories': categories,
    }
    return render(request, 'item/detail.html', context=data)