class Viber:
    d = {}

    @classmethod
    def add_message(cls, messg):  # добавление нового сообщения в список сообщений;
        cls.d[messg.text] = messg.fl_like

    @classmethod
    def remove_message(cls, messg):  # удаление сообщения из списка;
        del cls.d[messg.text]

    @classmethod
    def set_like(cls, messg):  # поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть, то убирается);
        if messg.fl_like == False:
            messg.fl_like = True
        else:
            messg.fl_like = False

    @classmethod
    def show_last_message(cls, digit):  # отображение последних сообщений;
        d1 = list(cls.d)
        return d1[-digit:]

    @classmethod
    def total_messages(cls):  # возвращает общее число сообщений.
        return len(cls.d)


class Message:
    def __init__(self, text, fl_like=False) -> None:
        self.text = text
        self.fl_like = fl_like
# text - текст сообщения (строка);
# fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False - в противном случае, изначально False);


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.show_last_message(1)
Viber.remove_message(msg)
