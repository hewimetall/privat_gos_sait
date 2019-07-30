from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from product_category.models import items_cat as Product
from pattern_for.models import pattern_for as pattern_for
from .cart import Cart
from .forms import CartAddProductForm ,Cart_one_prod


def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'],cat="shop")
    if request.is_ajax():
        return HttpResponse('OK')
    return redirect('/forma_obratnoj_svyazi')

def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_id)
    cart.remove(product)
    if request.is_ajax():
        return HttpResponse('OK')
    return redirect('cart:CartDetail')


def CartAdd_for(request,cat, product_id):
    cart = Cart(request)
    product =  get_object_or_404(pattern_for,categoy=cat, slug=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'],
                cat="usl")
        return render(request, 'cart/detail.html',
                 {'cart': cart})

@require_POST
def CartAdd_for_t(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(pattern_for, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('cart:CartDetail')

def CartRemove_for(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(pattern_for, slug=product_id)
    cart.remove(product)
    if request.is_ajax():
        return HttpResponse('OK')
    return redirect('cart:CartDetail')

def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html',
                 {'cart': cart})
