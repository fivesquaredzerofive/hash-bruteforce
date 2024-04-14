import hashlib
import itertools

def generate_strings(n):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLEMNOPQRSTUVWXYZ'
    for i in range(0, n+1):
        for combination in itertools.product(characters, repeat=i):
            yield ''.join(combination)

def sha256bruteforce():
    a = int(input("Input the length of the string: "))
    g = input("Input the hash: ")

    for string in generate_strings(a):
        b = string.encode('utf-8')
        if hashlib.sha256(b).hexdigest() == g:
            print(string)
            break;

def sha512bruteforce():
    a = int(input("Input the length of the string: "))
    g = input("Input the hash: ")

    for string in generate_strings(a):
        b = string.encode('utf-8')
        if hashlib.sha512(b).hexdigest() == g:
            print(string)
            break;

quest = input("Do you want to brute force sha256 or sha512?(sha256/sha512): ")
if quest == "sha256":
    sha256bruteforce()
elif quest == "sha512":
    sha512bruteforce()

