from .cart import Cart

# create a context processors so cart can works in all page

def cart(request):
    return {'cart': Cart(request)}