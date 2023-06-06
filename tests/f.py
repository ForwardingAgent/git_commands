from typing import Any


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 100

    def __init__(self, a, b, c) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    def setter(self, x):
        pass

    def __getattribute__(self, __name: str) -> Any:
        if __name == self.MIN_DIMENSION or __name == self.MAX_DIMENSION:
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

    @classmethod
    def check(cls, val):
        if cls.MIN_DIMENSION <= val <= cls.MAX_DIMENSION:
            return val




d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError