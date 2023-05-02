import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"


def password(n):
    while True:
        s = ''
        for i in range(n):
            indx = random.randint(1, len(chars) - 1)
            s += chars[indx]
        yield s


n = int(input())
[print(next(password(n))) for j in range(5)]
