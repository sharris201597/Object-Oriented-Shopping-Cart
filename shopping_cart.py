#Shopping Cart Made with classes

class Users():
    SHOPPED_BEFORE = True
    
    def __init__(self, user_name, password, shopping_cart, name):
        self.user_name = user_name
        self.password = password
        self.shopping_cart = shopping_cart
        self.name = name

    def crate_user(self):
        self.user_name = input("Enter your username: ")
        self.password = input("Enter password: ")
        

    def add2_cart(self):
        item = input("What else would you like to add to your cart? ")
        return self.shopping_cart.append(item)

    def del_from_cart(self):
        item = input("What else would you like to add to your cart? ")
        if item in self.shopping_cart:
            self.shopping_cart.remove(item)
            print(f"Here's whats left : {self.shopping_cart}")





sam = Users("Sam_2", "Bamdeandre12", ["Jeans", "Polo-shirt", "belt", "socks"], "Samuel Harris")




def run():
    while True:
        response = input('What would you like to do? Add/Delete/Show/Quit ')
        
        if response.strip().lower() == 'quit':            
            print('Sending you to checkout')
            print(f"Your cart: {sam.shopping_cart}")
            break
        elif response.strip().lower() == 'add':
            sam.add2_cart()
            
        elif response.strip().lower() == 'delete':
            sam.del_from_cart()
               
        elif response.strip().lower() == "show":
            print(f"Here's your cart: {sam.shopping_cart}")
        
        else:
            print("Please enter ADD/DELETE/SHOW/ or QUIT")
        
            
run()
