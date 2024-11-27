from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Category, Item
from .forms import NewItemForm, EditItemForm

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category = item.category, is_sold= False).exclude(pk=pk)[0:3]
    data = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'item/detail.html', context=data)

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    context = {
        'form':form,
        'title': 'New Item',
        'button_text': 'Create Item',
        'url': 'item-new',
        'form_action': 'new/',
    }

    return render(request, 'item/form.html', context=context)

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    context = {
        'form':form,
        'title': 'Edit Item',
        'button_text': 'Create Item',
        'url': 'item-new',
        'form_action': 'new/',
    }

    return render(request, 'item/form.html', context=context)

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index2')
