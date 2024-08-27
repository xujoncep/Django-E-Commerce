from store.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if any
        cart = self.session.get('session_key')

        #if the user is new 
        if 'session_key' not in request.session:
            cart = self.session['session_key']= {}

        #make sure cart is avilable on all the page of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        #logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True
    

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #get id from cart
        product_ids = self.cart.keys()
        #use id lookup product in dstsbsde moddel
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quantity(self):
        quantities = self.cart
        return quantities


    