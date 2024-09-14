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
    
    def total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantites = self.cart
        total = 0
        for key, value in quantites.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                         total = total + (product.price * value)
        return total



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


    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

		# Get cart
        ourcart = self.cart
		# Update Dictionary/cart
        ourcart[product_id] = product_qty
        
        self.session.modified = True
        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        # # Deal with logged in user
        # if self.request.user.is_authenticated:
        #     # Get the current user profile
        #     current_user = Profile.objects.filter(user__id=self.request.user.id)
        #     # Convert {'3':1, '2':4} to {"3":1, "2":4}
        #     carty = str(self.cart)
        #     carty = carty.replace("\'", "\"")
        #     # Save carty to the Profile Model
        #     current_user.update(old_cart=str(carty))