from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f'Базовый класс Model'


class ModelForm(Model):
    __id = 0

    def __init__(self, login: str, password: str) -> None:
        super().__init__()
        self._logon = login
        self._password = password
        __class__.__id += 1
        self._id = __class__.__id

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())