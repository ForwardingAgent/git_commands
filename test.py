
#def gen():
#  for i in range(2, 10001):
#    yield i #yield применяется там, где значение нужно отправить обратно вызывающей стороне. 
#    # Но в отличие от return, выхода из функции в данном случае не происходит. Вместо этого, при возврате состояние функции запоминается. 
#    
#gen = gen()

#def flip(func):
#    def inner(*args, **kwargs):
#        print(type(args))
#        a = reversed(args)
#
#        return func(*a, **kwargs)
#    return inner
#
#@flip
#def div(x, y, show=False):
#    res = x / y
#    if show:
#        print(res)
#    return res
#
#div(2, 4, show=True)
##################


def my_print(func):
    def inner(*args, **kwargs):
        args = list(args)
        args = [i.upper() if type(i) is str else i for i in args]
        kwargs = {k: v.upper() if type(v) is str else v for k, v in kwargs.items()}
        return func(*args, **kwargs)

    return inner


print = my_print(print)

print('hi', 'there', end='!')
print(111, 222, 333, sep='xxx')
# divbythree = [  "Yes" if number % 3 == 0 else "No" for number in range(1,20)]
