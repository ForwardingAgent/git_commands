class Test:
    x = 1
    y = 2

    def __init__(self):
        self.x = 3
        self.y = 4

    @staticmethod
    def static_method(x, y):
        a = x + y
        b = self.x + self.y  # <-- ОШИБКА не понимает, что такое self
        c = cls.x + cls.y  # <-- ОШИБКА не понимает, что такое cls
        d = Test.x + Test.y
        return a, b, c, d

    @classmethod
    def class_method(cls, x, y):
        a = x + y
        b = self.x + self.y  # <-- ОШИБКА не понимает, что такое self
        c = cls.x + cls.y
        d = Test.x + Test.y
        return a, b, c, d

    def self_method(self, x, y):
        a = x + y
        b = self.x + self.y
        c = cls.x + cls.y  # <-- ОШИБКА не понимает, что такое cls
        d = Test.x + Test.y
        return a, b, c, d

    def func_method(x, y):  # <-- ОШИБКА пихает в х ссылку на объект, ошибка при вызове
        a = x + y  # <-- ОШИБКА ^
        b = self.x + self.y  # <-- ОШИБКА ^
        c = cls.x + cls.y  # <-- ОШИБКА ^
        d = Test.x + Test.y
        return a, b, c, d

    def empty_method():  # <-- ОШИБКА не знает куда бы запихнуть ссылку на объект
        return 123