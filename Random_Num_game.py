import random
print("Hello, User!", "Let's play!", sep="\n")
random_number = random.randint(1, 100)
print("Give your number: ")
n = int(input())
while(n != random_number):
    if n > random_number:
        print("Your number is bigger. Try again")
        n = int(input())
    elif n < random_number:
        print("Your number is lower. Try again")
        n = int(input())
if n == random_number:
    print("Yes! The numer is: ", n)
