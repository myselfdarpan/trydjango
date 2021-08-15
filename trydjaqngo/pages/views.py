from django.http import HttpResponse
from django.shortcuts import render
from products.models import Products

# Create your views here.

def home_view(request, *args, **kwargs):
        return render(request, 'home.html', {})

def contact(request, *args, **kwargs):
        my_dict = {
            'name':'darpan',
            'age':35,
            'lister': [1, 23, 54, 123]
        }
        return render(request, 'contact.html', my_dict)

def product_detail(request):
    obj = Products.objects.all()
    # context = {
    #     'title':obj.name,
    #     'description': obj.description,
    #     'price': obj.price
    # }
    context = {
        'object': obj
    }
    return render(request, 'product_details.html', context)