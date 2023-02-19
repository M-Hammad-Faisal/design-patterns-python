from __future__ import annotations
from abc import ABC, abstractmethod


class Product:

    def __init__(self, name: str = None, price: int=None):
        """Create a product with name and price"""
        self.__name = name
        self.__price = price

    def get_name(self):
        """Get name of Product."""
        return self.__name

    def set_name(self, name: str):
        """Set name of Product."""
        self.__name = name

    def get_price(self):
        """Get price of Product."""
        return self.__price

    def set_price(self, price: int):
        """Set price of Product."""
        self.__price = price


class Box(ABC):

    def __init__(self):
        """Create a box with child and product attributes."""
        self.__child = None
        self.__product = []

    def get_child(self):
        """Return true if box has any Child \n child : Boolean"""
        return self.__child

    def set_child(self, child: bool):
        """Set child of box. \n child: Boolean"""
        self.__child = child

    def get_product(self):
        """Get products in the box."""
        return self.__product

    def set_product(self, product: Product):
        """Set products in the box."""
        self.__product.append(product)


class Order(Box):

    def __init__(self, reciept: Product):
        """Create an order with reciept. \n reciept: Product"""
        super().__init__()
        self.__boxes = [reciept]

    def add(self, box: Box):
        """Add box in order."""
        self.__boxes.append(box)

    def remove(self, box: Box):
        """Remove box in order."""
        self.__boxes.remove(box)

    def get_boxes(self):
        """Get all boxes in order."""
        return self.__boxes

    def __calculate_price(self, boxes: list):
        """Get prices of given boxes."""
        total_price = 0
        for box in boxes:

            if type(box) == Product:
                total_price += box.get_price()
                continue

            if box.get_child():
                total_price += self.__calculate_price(box.get_product())

            else:
                for product in box.get_product():
                    total_price += product.get_price()

        return total_price

    def get_price(self):
        """Get prices of all boxes in order."""
        total_price = self.__calculate_price(self.__boxes)
        return total_price

if __name__ == "__main__":
    # Create a reciept of order
    reciept = Product(name="Reciept", price=10)

    # create an order
    order = Order(reciept)

    # create a phone and headphone
    phone = Product(name="Phone", price=20000)
    headphones = Product(name="HeadPhones", price=2000)

    # create a box and put phone and headphone in a box
    phone_headphone_box = Box()
    phone_headphone_box.set_product(product=phone)
    phone_headphone_box.set_product(product=headphones)

    # create a charger and put it in a box
    charger = Product(name="Charger", price=1200)
    charger_box = Box()
    charger_box.set_product(product=charger)

    # create a hammer and put it in a box
    hammer = Product(name="Hammer", price=800)
    hammer_box = Box()
    hammer_box.set_product(product=hammer)

    # create a box and put phone_headphone_box and charger_box in a box
    phone_headphone_charger_box = Box()
    phone_headphone_charger_box.set_child(True)
    phone_headphone_charger_box.set_product(phone_headphone_box)
    phone_headphone_charger_box.set_product(charger_box)

    # add all boxes to order
    order.add(box=hammer_box)
    order.add(box=phone_headphone_charger_box)

    # get total price of order
    total_price = order.get_price()
    print(total_price)

    # Furthermore, Image is added in images folder,
    # for pictorial view of current Example
