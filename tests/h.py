# OOP Balakirev 1.7.11
class AppStore:
    def __init__(self) -> None:
        self.d = {}

    def add_application(self, app):  # добавление нового приложения app в магазин;
        self.d[app.name] = app.blocked
        print(self.d)

    def remove_application(self, app):  # удаление приложения app из магазина;
        del self.d[app]
        print(self.d)

    def block_application(self, app):  # блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
        app.blocked = True
        print(self.d)

    def total_apps(self):  # возвращает общее число приложений в магазине.
        return len(self.d)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.block_application(app_youtube)
print(store.total_apps())
store.remove_application(app_youtube)

