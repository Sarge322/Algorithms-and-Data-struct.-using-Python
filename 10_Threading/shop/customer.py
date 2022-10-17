class Customer:

    def __init__(self):
        self.name = None
        self.basket = None
        self.status = None

    def setName(self, new_name):
        self.name = new_name

    def take_basket(self, basket):
        self.basket = basket

    def setStatus(self, status):
        self.status = status

    def get_basket(self):
        return self.basket

    def take_goods(self, goods_taken):
        self.basket.set_goods(goods_taken)

    def choose_goods(self, goods_list):
        pass

    def getName(self):
        return self.name
