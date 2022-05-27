# Python Programs
Just programs for fun and to keep me thinking.

[FreeCodeCamp Python Tasks](https://replit.com/@RonaldGRowe)

## MaxSubArray Script
### Operation
* uses for loops to run through all combinations and store highest sum
* O(n2) to slow to pass some tests
* returns highest possible sum from continuous digits from list of ints
### Still Finishing
* need to look for linear approach
* look at eliminating bad combinations
* ex: list = [-5,3,-4,10,5,1,4] first three ints only bring value down, should be excluded

### minStack
### Operation
* uses a class to handle creating and working with a stack data structure
* passes in values, stores a min and top value for instant recall O(1) constant time
### Still Finishing
* need to look at other data structures like linked list, queues, binary trees
* need to look at other options besides classes

### Parentheses
### Operation
* determines if the paratheses are in the correct order
* creates a left and right side value where left>=right if right is larger then it is out of order
### Still Finishing
* missed part about tracking order of different types of parethenses
* need to implment script to track current left side bracket and fail if wrong right bracket or not a new left bracket
* might be good to use a stack structure!!!

## Prime Numbers Script
### Operation
* takes user input for a max number
* finds all prime numbers up to max
* returns list and total number of prime numbers
### Still Finishing
* need to create test script for this program
* working on finding max input
* found out python3 is capable of using numbers as big as memory will allow
* working on reducing runtime
### Learned
* found out while loop was slower than for loop 
* .0782065 seconds faster for 10k numbers
* 5.163216 seconds faster for 100k number
* also incrementing numerator by 2 was used to eliminate even options
* this only allowed for minimal gains
* .0144697 seconds faster for 10k numbers incremented by 2 vs 1
* .8526902 seconds faster for 100k numbers incremented by 2 vs 1
* so far max input of 500k numbers a total of 41,538 prime numbers took 144.6112232 secs

### RotateArray
### Operation
* reverses a list of elements
* pulls values from end of list 
### Still Finishing
* need to look for other options for handlind this

## Stock Price Script
### Operation 
* buys at low price and sells at high
* maxamizing profit
* returns profit
* my first leetcode
### Working On
* got it running
* going to try more of these tasks to keep my mind working
* going to create some test to run on this program

### TwoSums
### Operation
* adds two numbers from list to check for target number and returns index of numbers in list
* cannot use same index twice
* created a for loop version O(n2) and while loop linear version O(n)
### Still Finishing
* Need to look at other algorithms to tackle this problem.
