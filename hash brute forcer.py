import hashlib
import itertools

def generate_strings(n):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLEMNOPQRSTUVWXYZ'
    for i in range(0, n+1):
        for combination in itertools.product(characters, repeat=i):
            yield ''.join(combination)



a = int(input("Input the length of the string: "))
g = input("Input the hash: ")

for string in generate_strings(a):
    b = string.encode('utf-8')
    if hashlib.sha256(b).hexdigest() == g:
        print(string)
        break;