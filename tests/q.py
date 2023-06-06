# потерял
class PolyLine:
    def __init__(self, start_coord, *args) -> None:
        self.start_coord = start_coord
        self.args = [*args]

    @classmethod
    def add_coord(x, y):  # добавление новой координаты (в конец);
        self.x = x
        self.y = y

    @classmethod
    def remove_coord(indx):  # удаление координаты по индексу (порядковому номеру, начинается с нуля);
        self.indx = indx

    def get_coords():  #получение списка координат (в виде списка из кортежей).


# TEST-TASK___________________________________

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
assert hasattr(poly, 'add_coord') and hasattr(poly, 'remove_coord') and hasattr(poly, 'get_coords') and \
       callable(poly.add_coord) and callable(poly.remove_coord) and callable(poly.get_coords), \
    "ошибка, не все методы есть в экземпляре класса"

poly.get_coords()
assert poly.get_coords() == [(1, 2), (3, 5), (0, 10), (-1, 8)], \
    "метод get_coords() вернул неправильный формат данных"

poly.add_coord(10, 20)
assert poly.get_coords()[-1] == (10, 20), "метод add_coord() работает некорректно"

poly.remove_coord(0)
poly.remove_coord(-1)
assert poly.get_coords() == [(3, 5), (0, 10), (-1, 8)], "метод remove_coord() работает некорректно"
print("Правильный ответ !!")