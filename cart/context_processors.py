from .cart import Cart

# create a context processors so our cart can works in all page

def cart(request):
    #return deault data
    return {'cart': Cart(request)}