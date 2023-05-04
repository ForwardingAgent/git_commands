class PathLines:
    def __init__(self, *args):
        self.lst = [*args]

    def get_path(self):  # возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
        return self.lst

    def get_length(self):  # возвращает суммарную длину пути (сумма длин всех линейных сегментов);
        self.summa_leight = []
        if len(self.lst) == 0:
            return 0
        elif len(self.lst) > 1:
            for i, v in enumerate(self.lst[:-1]):
                leight = ((self.lst[i + 1].x - v.x) ** 2 + (self.lst[i + 1].y - v.y) ** 2) ** 0.5
                self.summa_leight.append(leight)
        self.summa_leight.append((self.lst[0].x ** 2 + self.lst[0].y ** 2) ** 0.5)  # от 0 до первой координаты
        return sum(self.summa_leight)

    def add_line(self, line):  # добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
        self.line = line
        self.lst.append(self.line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# TEST-TASK___________________________________
p = PathLines(LineTo(1, 2))
assert p.get_length() == 2.23606797749979, "неверный вывод должно быть: 2.23606797749979"

p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
#assert p.get_length() == 28.191631669843197, "неверный вывод должно быть: 28.191631669843197"
assert p.get_length() == 28.1916316698432, "неверный вывод должно быть: 28.1916316698432"

m = p.get_path()
assert all(isinstance(i, LineTo) for i in m) and len(m) == 3, "неверный вывод должно быть: True"

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
assert h.get_length() == 71.8992593599813, "неверный вывод должно быть: 71.8992593599813"

k = PathLines()
assert k.get_length() == 0, "неверный вывод должно быть: 0"

assert k.get_path() == [], "неверный вывод должно быть: [] (пустой список)"
print("Правильный ответ !")

p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True ----или False???

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []