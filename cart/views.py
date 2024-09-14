from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quantity
    totals = cart.total()
    return render(request, 'cart_summary.html',{'cart_products':cart_products, 'quantities':quantities,'totals':totals})

def cart_add(request):
    #get the cart
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # product look into db
        product = get_object_or_404(Product, id=product_id)
        #save to session
        cart.add(product=product, quantity=product_qty)
        #get cart quantity
        cart_quantity = cart.__len__()
        #return response
        response = JsonResponse({'quantity:':cart_quantity})
        messages.success(request, "Item Added In Your Shopping Cart!")
        return response

def cart_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        # Get product ID from POST request
        product_id = int(request.POST.get('product_id'))
        
        # Call delete function in Cart
        cart.delete(product=product_id)

        # Prepare the JSON response
        response = JsonResponse({'product': product_id})
        
        # Display success message to the user
        messages.success(request, "Item Deleted From Shopping Cart!")
        
        return response


def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
		messages.success(request, ("Your Cart Has Been Updated!"))
		return response
