from django.shortcuts import render, get_object_or_404, redirect
from .models import Products
from .forms import ProductForm

# Create your views here.

def dynamic_view(request, my):
    obj = get_object_or_404(Products, id=my)
    context = {
        'object': obj
    }
    return render(request, 'product_details.html', context)


def delete_view(request, my):
    obj = get_object_or_404(Products, id=my)
    if request.method == 'POST':
        obj.delete()
        print('post')
        return redirect('../../../')
    context = {
        'object': obj
    }
    print('get')
    return render(request, 'product_delete.html', context)

def product_list(request):
    queryset = Products.objects.all()
    context = {
        'object': queryset
    }
    return render(request, 'product_list.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'product_create.html', context)

def product_details(request):
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
