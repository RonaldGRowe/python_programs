#!/usr/bin/env python3

#import numpy as np
import time


#primeList = np.array([2])
primeList = [2]
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
    startsec = time.perf_counter()
#initialize the starting number to start with int 3
    startNum = 3
#loop through numbers to be checked
    while startNum <= int(maxNum):

        z = 0

        for p in primeList:

            if startNum % p == 0:

                startNum+=2

                break

            else:

                 z+=1

#add prime factor to primeList

        if z == len(primeList):
#            primeList = np.append(primeList, startNum)
            primeList.append(startNum)
            startNum+=2

#determine if plural

    numbers = "numbers" 
    if len(primeList)  == 1:
        numbers = "number"

#display results
    print(f"List of prime numbers up to {maxNum}{chr(10)}{primeList}")

    print(f"{len(primeList)} prime {numbers}")

    stopsec = time.perf_counter()

    print(round(stopsec-startsec, 8))

    return primeList


if __name__ == "__main__":
    check_numbers(get_user_input())
