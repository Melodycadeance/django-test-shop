from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def items_list(request):
    items = Item.objects.filter().order_by('title')
    return render(request, 'shop/items_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {'item': item})