import random

print('Welcome to the Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+-.,?@^'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Enter desired password length: ')
length = int(length)

print('\here are your passwords: ')

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)