'''
Exercise 1: Turn the shopping cart program from yesterday into an object-oriented program
'''


class Cart:
    def __init__(self, name: str):
        self.cart = {}
        self.name = name

    def add(self, item, quantity: int):
        item = item.upper()
        self.cart[item] = self.cart.get(item, 0) + quantity

    def remove(self, item, quantity: int):
        item = item.upper()
        if item not in self.cart:
            return "This item does not exist in your cart."
        self.cart[item] = self.cart.get(item, 0) - quantity
        if self.cart[item] == 0:
            del self.cart[item]

    def show(self):
        if self.cart:
            print(f"\n{self.name}'s SHOPPING CART")
            for k, v in self.cart.items():
                print(f"Item: {k} - Quantity: {v}")
        else:
            return "Your cart is currently empty"


my_cart = Cart("YY")
result = (my_cart.show())
print(type(result))
