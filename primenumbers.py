#!/usr/bin/env python3

import time

#initialize a list of prime numbers

primeList = [2]

#check user input for errors

while True:

    try:

        maxNum = int(input("Enter whole number greater than 1: "))

        if maxNum <= 1:

            raise ValueError("Enter whole number greater then 1. -")

        break

    except ValueError:

        print("Whole number required, >1. -")

#initialize the starting number to start with int 2

startNum = 3

startsec = time.perf_counter()

#loop through numbers to be checked

while startNum <= int(maxNum):

    z = 0

#checking for 0 remainder, will not be prime

#    if startNum % primeList[z] == 0:

 #       startNum+=1

#    else:

#if remainder is > 0 increase z by 1

#z determines the prime factor used

#         z+=1

#loop through prime factors

    for p in primeList:

        if startNum % p == 0:

            startNum+=2

            break

        else:

             z+=1

#add prime factor to primeList

    if z == len(primeList):

        primeList.append(startNum)

        startNum+=2

#determine if plural

if len(primeList)  == 1:

    numbers = "number"

else:

     numbers = "numbers" 

#display results

print("List of prime numbers up to "+str(maxNum)+"\n"+str(primeList))

print(str(len(primeList))+ " prime "+numbers)

stopsec = time.perf_counter()

print(round(stopsec-startsec, 8))

