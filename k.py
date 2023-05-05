class Animal:
    def __init__(self, name: str, kind: str, old: int) -> None:
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def var(self):
        return self.__old
    
    @vars.setter
    def var(self, *args):
        self.args = args
        for i in args:
            if i == name:
                self.__name = name
            elif i == kind:
                self.__kind = kind
            elif i == old:
                self.__old = old


cat = Animal('Васька', 'дворовый кот', 5)
dog = Animal('Рекс', 'немецкая овчарка', 8)
bird = Animal('Кеша', 'попугай', 3)
