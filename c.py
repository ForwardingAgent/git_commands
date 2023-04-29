
#ООП 1.5.9
class Cart:

    def __init__(self) -> None:
        self.goods = []

    def add(self, gd):  # добавление в корзину товара, представленного объектом gd;
        self.gd = gd
        self.goods.append(self.gd)

    def remove(self, indx):  # удаление из корзины товара по индексу indx;
        self.indx = indx
        self.goods.pop(self.indx)

    def get_list(self):  # получение из корзины товаров в виде списка из строк:
        return [f"{i.name}: {i.price}" for i in self.goods]


class Table:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price



cart = Cart()
cart.add(TV('toshiba', 2000))
cart.add(TV('samsung', 3000))
cart.add(Table('ikea', 4000))
cart.add(Notebook('Ibm', 10000))
cart.add(Notebook('Lenovo', 30000))
cart.add(Cup('mug', 500))
# cart = Cart
# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1= Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)
# cart.add(tv1)
# cart.add(tv2)
# cart.add(t)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)