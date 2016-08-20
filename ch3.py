#!/usr/bin/python 

#Collatz Sequence practice
def collatz(number):
    newnum = 0
    if number == 1:
        return 0
    elif number %2 == 0:
        newnum = number/2
        print(int(newnum))
        collatz(newnum)
    elif number %2 ==1:
        newnum = 3*number +1
        print(int(newnum))
        collatz(newnum)
        
print("Please enter a number greater than zero:")
number = 0

while number ==0:
    try:
        number = int(input())
    except ValueError:
        print("Error: Entry has to be a number greater than zero")

collatz(number)
