#!/bin/usr/env python3
import sys

#Leetcode still some tests to pass, possibly timing out with this slow process 201/209 8 to go.
def maxSubArray(nums):
        maxtotal = None
        total = None
        i = 0
#handle string in terminal input
        numlist = nums.split(",")
        while i < len(numlist):
            total = int(numlist[i])
            print(total, maxtotal)
            if maxtotal == None or total > maxtotal:
                maxtotal = total
                print(maxtotal)
            for n in numlist[i+1:]:
                total += int(n)
                if total > maxtotal:
                    maxtotal = total
            i += 1
        return maxtotal
if __name__ == "__main__":
    print(maxSubArray(sys.argv[1]))
