from django.shortcuts import render
from .models import Item

# Create your views here.

def items_list(request):
    items = Item.objects.filter().order_by('title')
    return render(request, 'shop/items_list.html', {'items': items})