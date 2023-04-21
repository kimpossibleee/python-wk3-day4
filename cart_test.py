import unittest
from shopping_cart import Cart

class TestCart(unittest.TestCase):

    def test_add(self):
        my_cart = Cart('yy')
        my_cart.add("Cookies", 2)
        result = my_cart.cart
        expected = {'COOKIES': 2}
        self.assertEqual(result, expected)

    def test_remove(self):
        my_cart = Cart('yy')
        result = my_cart.remove("water", 3)
        expected = "This item does not exist in your cart."
        self.assertEqual(result, expected)

    def test_print(self):
        my_cart = Cart('yy')
        result = my_cart.show()
        self.assertEqual(result, "Your cart is currently empty")
        # things to note: printing the result will not work because the method .show() will return a <class 'NoneType'>. Therefore, you would have to return the string instead of printing it.

if __name__ == '__main__':
    unittest.main()
