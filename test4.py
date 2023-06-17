class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.goods = []

    def add_product(self, product):
        self.product = product
        self.goods.append(self.product)

    def remove_product(self, product):
        self.goods.remove(self.product)


class Product:
    id_cls = 0

    def __init__(self, name: str, weight: int or float, price: int or float):
        __class__.id_cls += 1
        self.id = __class__.id_cls
        self.name = name
        self.weight = weight
        self.price = price

    def __delattr__(self, attr):
        if attr == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

    def __setattr__(self, key, value):
        if key == 'id' and type(value) is not (int or float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'name' and type(value) is not str:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'weight' and type(value) is not (int or float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'price' and type(value) is not (int or float):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)
#
#
## TEST-TASK___________________________________
#assert issubclass(Shop, object), "Класс Book не является подклассом object, скорее всего не создан"
#assert issubclass(Product, object), "Класс Product не является подклассом object, скорее всего не создан"
#
## проверка атрибутов в классах
shop = Shop("Балакирев и К")
## проверка названия
#assert 'Балакирев и К' in shop.__dict__.values(), "ошибка в инициализаторе, не создается название магазина "
#
#assert hasattr(shop, "goods"), "Не создан локальный атрибут - goods"
#assert hasattr(shop, 'add_product'), "Метод add_product не определен в объекте"
#assert hasattr(shop, 'remove_product'), "Метод add_product не определен в объекте"
#
## проверка атрибутов в классах
#book = Product("Python ООП", 100, 1024)
#
#assert hasattr(book, 'id'), "Не создан локальный атрибут - id"
#assert type(book.id) == int, "номер id должен быть целым числом"
#
#assert hasattr(book, 'weight'), "Не создан локальный атрибут - weight"
#assert type(book.weight) in (int, float) and book.weight > 0, \
#    "weight должен быть целое или вещественное положительное число"
#
#assert hasattr(book, 'price'), "Не создан локальный атрибут - price"
#assert type(book.price) in (int, float) and book.price > 0, \
#    "price должна быть целое или вещественное положительное число "
#
## проверка, что номера id уникальны
#lst = [Product("Python ООП", 100, 1024).id for _ in range(0, 3)]
#assert any(False if lst[_] in lst[_ + 1:] else True for _ in range(len(lst))), "ошибка id не уникальны !!!"
#
# проверка add_product
shop.add_product(Product("Python ООП", 100, 1024))
x = Product("Test", 10, 10)
shop.add_product(x)
assert shop.goods[1] == x, "метод add_product отработал некоректно"

# проверка remove_product
shop.remove_product(x)
assert x not in shop.goods, "метод remove_product отработал некоректно"

try:
    del x.id
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError при попытке удаления из продукта, атрибута id"

print("Правильный ответ !")