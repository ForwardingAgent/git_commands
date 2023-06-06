cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

gen = (cities[i % len(cities)] for i in range(1000000))
for j in range(20):
    print(next(gen), end=' ')

# def unit():
#     gen = (x for x in cities)
#     for i in range(1000000):
#         if i != len(cities):
#             print(next(gen), end=' ')
#         else:
#             unit()
