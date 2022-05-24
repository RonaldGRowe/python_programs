#!/bin/usr/env python3

#Leetcode 2 sums different approach
import sys

def twosums(nums, target):
        f=0
        l=-1
        while f < nums.index(nums[l], f+1):
            if nums[f] + nums[l] == target:
                return [f,nums.index(nums[l], f+1)]
            i=1
            while i < (nums.index(nums[l])-f):
                if nums[f] + nums[f+i] == target:
                    return [f,f+i]
                if nums[l] + nums[l-i] == target:
                    return [nums.index(nums[l], (nums.index(nums[l-i])+1)), nums.index(nums[l-i])]
                i += 1
            f += 1
            l -= 1


if __name__ == "__main__":
    print(twosums(sys.argv[1], sys.argv[2]))
