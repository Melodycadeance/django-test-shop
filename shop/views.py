from django.shortcuts import render

# Create your views here.

def items_list(request):
    return render(request, 'shop/items_list.html', {})