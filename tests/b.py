import random

my_set = ()
while len(my_set) != 7:
    my_set.add(random.randrange(1, 50))
print(*sorted(my_set))