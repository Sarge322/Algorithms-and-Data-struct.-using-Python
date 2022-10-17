class Cashier:

    def __init__(self, name):
        self.name = name
        self.open = None
        self.busy = None

    def payment(self, customer):
        current_basket = customer.get_basket()
        paycheck = 0
        for i in current_basket:
            paycheck = paycheck + int(i[1])
        return paycheck


class Cust:
    def __init__(self):
        self.basket = None

    def get_basket(self):
        self.basket = [[1, 1], [2, 2], [3, 3], [4, 4]]
        return self.basket


c = Cashier('1')
c1= Cust()
print(c1.get_basket())

print(c.payment(c1))
