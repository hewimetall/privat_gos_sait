from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from product_category.models import items_cat as Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    if request.is_ajax():
        return HttpResponse('OK')

    return redirect('cart:CartDetail')

def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_id)
    cart.remove(product)
    if request.is_ajax():
        return HttpResponse('OK')
    return redirect('cart:CartDetail')

def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html',
                 {'cart': cart})
