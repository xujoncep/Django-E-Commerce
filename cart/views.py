from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    return render(request, 'cart_summary.html',{})

def cart_add(request):
    #get the cart
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        # product look into db
        product = get_object_or_404(Product, id=product_id)
        #save to session
        cart.add(product=product)
        #get cart quantity
        cart_quantity = cart.__len__()
        #return response
        response = JsonResponse({'quantity:':cart_quantity})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass

