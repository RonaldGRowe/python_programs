#!/usr/bin/env python3

#import numpy as np
import time
from math import sqrt

#primeList = np.array([2])
#check user input for errors


def get_user_input():
    message = "Enter whole number greater than 1: "
    while True:
        try:
            maxNum = int(input(message))
            if maxNum <= 1:
                raise ValueError
            return maxNum

        except ValueError:
            print("Check input value")




def check_numbers(maxNum):
    primeList = [2]
    startsec = time.perf_counter()
    startsec2 = time.perf_counter()
#initialize the starting number to start with int 3
#loop through numbers to be checked
    factorlist = [2]
    for startNum in range(3,maxNum+1, 2):
        for p in primeList[primeList.index(factorlist[-1])+1:]:
            if p >= (sqrt(startNum)+1):
                break
            else:
                factorlist.append(p)
        for f in factorlist:
            if startNum % f == 0:
                break
            else:
                if f == factorlist[-1]:
#add prime factor to primeList
                    primeList.append(startNum)
                    break
        if not factorlist:
            primeList.append(startnum)
    stopsec2 = time.perf_counter()
#determine if plural

    numbers = "numbers" 
    if len(primeList)  == 1:
        numbers = "number"

#display results
    print(f"List of prime numbers up to {maxNum}{chr(10)}{primeList}")

    print(f"{len(primeList)} prime {numbers}")

    stopsec = time.perf_counter()

    print(round(stopsec-startsec, 8))
    print(round(stopsec2-startsec2, 8))
    return primeList


if __name__ == "__main__":
    check_numbers(get_user_input())
