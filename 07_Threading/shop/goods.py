from shop.file_reader import file_reader


class Goods:
    def __init__(self):
        self.goods_list = None

    def create_goods_list(self):
        self.goods_list = file_reader('goods_list.txt')

    def getGoods(self):
        return self.goods_list


