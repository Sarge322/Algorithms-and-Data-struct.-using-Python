class Basket:

    def __init__(self, num):
        self.number = num
        self.free = True
        self.goods = []

    def get_number(self):
        return self.number

    def set_goods(self, goods):
        self.goods = goods

    def get_goods(self):
        return self.goods
