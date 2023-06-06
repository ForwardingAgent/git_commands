# 2.3.10
class Bag:
    _things = []

    def __init__(self, max_weight) -> None:
        self.max_weight = max_weight
        self.things = self._things
        
    def add_thing(self, thing):  # добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
        self.thing = thing
        if self.max_weight > self.thing.weight:
            self.things.append(self.thing)
            self.max_weight -= self.thing.weight

    def remove_thing(self, indx):  # удаление предмета по индексу списка __things;
        self.max_weight += self.thing[indx].weight
        del __class__.__things[indx]

    def get_total_weight(self):  # возвращает суммарный вес предметов в рюкзаке.
        res = 0
        for i in self.things:
            res = res + i.weight
        return res


class Thing:
    def __init__(self, name: str, weight: (int or float)) -> None:
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")