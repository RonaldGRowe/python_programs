#!/bin/usr/env python3


#More Leetcode fun the obvious for loops
#working on different method of traversing list
def twosums(numslist):
    for n in nums[0:-1]:
        for sn in nums[nums.index(n)+1:]:
            if n+sn == target:
                if n != n:
                    return [nums.index(n), nums.index(sn)]
                return [nums.index(n), nums.index(sn, nums.index(n)+1)]
