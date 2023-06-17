from functools import reduce
from operator import * 


def evaluate(coefficients, x):
    lst_index = [j for j in range(len(coefficients))]
    return list(map(lambda a, b: int(a) * pow(x, b), coefficients, reversed(lst_index)))        


coefficients = [10, 10, 10, 10, 10]  # input().split()
x = 2  # int(input())
print(evaluate(coefficients, x))
