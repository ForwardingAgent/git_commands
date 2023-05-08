class Complex:
    def __init__(self, real: (int or float), img: (int or float)) -> None:
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real
    
    @real.setter
    def real(self, real):
        if type(real) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__real = real

    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self, img):
        if type(img) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__img = img

    def __abs__(self, cm):
        self.cm = cm
        c_abs = (cm.real * cm.real + cm.img * cm.img) ** 0.5
        return c_abs


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
print(abs(cmp))
