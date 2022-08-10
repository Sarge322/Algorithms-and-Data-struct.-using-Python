from shop.basket import Basket
import random


class BasketShelf:
    def __init__(self):
        self.basket = 50
        self.shelf = []

    def create_basket(self):
        for i in range(0, self.basket):
            self.shelf.append(Basket(i))

    def basket_to_go(self):
        while True:
            num = random.randint(self.basket)
            if self.shelf[num].free:
                return self.shelf.pop(num)

    def leave_basket(self, basket):
        self.shelf.append(basket)

    def is_empty(self):
        return self.shelf == []
