class Food:
    def __init__(self, name, weight, calories) -> None:
        self.name = name
        self.weight = weight
        self.calories = calories


class BreadFood(Food):  # white - True для белого хлеба, False - для остальных
    def __init__(self, name, weight, calories, white) -> None:
        super().__init__(name, weight, calories)
        self.white = white


class SoupFood(Food):  # dietary - True для диетического супа, False - для других видов
    def __init__(self, name, weight, calories, dietary) -> None:
        super().__init__(name, weight, calories)
        self.dietary = dietary


class FishFood(Food):  # fish - вид рыбы (семга, окунь, сардина и т.д.)
    def __init__(self, name, weight, calories, fish) -> None:
        super().__init__(name, weight, calories)
        self.fish = fish


bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")
print(bf.__dict__)