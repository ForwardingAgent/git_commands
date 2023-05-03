class PathLines:
    def __init__(self):
        self.lst = []

    def get_path(self):  # возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
        return self.lst

    def get_length(self):  # возвращает суммарную длину пути (сумма длин всех линейных сегментов);
        leight = sqrt((x1-x0) ** 2 + (y1 - y0) ** 2)

        return len(self.)

    def add_line(self, line):  # добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
        self.line = line
        self.lst.append(self.line)


class Line:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
