import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Hoeveel wachtwoorden wil je creëren: ')
number = int(number)

length = input('Hoe lang moeten de wachtwoorden zijn: ')
length = int(length)

print('\nHier zijn jouw wachtwoorden: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)