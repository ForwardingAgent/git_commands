# Вводится целое положительное число a. Необходимо определить генератор, 
# который бы возвращал модули чисел в диапазоне [-a; a], а затем еще один, 
# который бы вычислял кубы чисел (возведение в степень 3), возвращаемых первым генератором.
# Вывести в одну строчку через пробел первые четыре значения. 
# (Полагается, что генератор выдает, как минимум четыре значения).
# Sample Input:
# 3
# Sample Output:
# 27 8 1 0
def decor_cube(func):
    def wrapper(lim_num):
        return (x**3 for x in func(lim_num))
    return wrapper
@decor_cube
def gen_num(a):
    return (abs(x) for x in range((-1)*a, a+1))


gen_cube = gen_num(int(input()))
for x in range(4):
    print(next(gen_cube), end=' ')