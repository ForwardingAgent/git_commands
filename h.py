class AppStore:
    def __init__(self) -> None:
        self.d = {}

    def add_application(self, app):  # добавление нового приложения app в магазин;
        self.d[app] = Application.blocked

    def remove_application(self, app):  # удаление приложения app из магазина;
        self.d.remove(app)

    def block_application(self, app):  # блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
        if self.d[app] is False:
            self.d[app] is True

    def total_apps(self):  # возвращает общее число приложений в магазине.
        return len(self.d)


class Application:
    def __init__(self, name) -> None:
        self.name = name
        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
