
#def gen():
#  for i in range(2, 10001):
#    yield i #yield применяется там, где значение нужно отправить обратно вызывающей стороне. 
#    # Но в отличие от return, выхода из функции в данном случае не происходит. Вместо этого, при возврате состояние функции запоминается. 
#    
#gen = gen()

def decrypt(encrypted_text, n):
    if n == 0:
        return encrypted_text
    else:
        s1 = ''
        s2 = ''
        for i, v in enumerate(encrypted_text):
            if i % 2 != 0:
                s1 += v
            else:
                s2 += v
        encrypted_text = s1 + s2
        n -= 1
        decrypt(encrypted_text, n)
    # return encrypted_text

def encrypt(text, n):
    pass


print(decrypt("This is a test!", 2))  # "s eT ashi tist!"))
