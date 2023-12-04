# Day 5 Project - Random Password Generator
import random

typelist = ["C", "S", "N"]
charlist = [chr(97 + x) for x in range(26)] + [chr(65 + z) for z in range(26)]
symlist = [chr(33 + y) for y in range(15)]
numlist = [chr(48 + w) for w in range(10)]
password = []

print("Welcome to password generator")
charflag = int(input("How many letters in the password?\n"))
numflag = int(input("How many numbers in the password?\n"))
symflag = int(input("How many symbols in the password?\n"))

passlength = charflag + numflag + symflag
n = 0

while n < passlength:
    pick = random.choice(typelist)
    if pick == "C":
        if charflag > 0:
            password.append(random.choice(charlist))
            charflag -= 1
        else:
            n -= 1
    if pick == "S":
        if symflag > 0:
            password.append(random.choice(symlist))
            symflag -= 1
        else:
            n -= 1
    if pick == "N":
        if numflag > 0:
            password.append(random.choice(numlist))
            numflag -= 1
        else:
            n -= 1
    n += 1

password = "".join(password)
print(password)
