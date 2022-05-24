#!/bin/usr/env python3

#Leetcode Minstack problem
#passes 30 out of 31 tests??? possibly going so fast not enough time to log the new value into memory before checking
#Fixed using min value of list instead of just waiting for value to be assigned.

Class Minstack:
   def __init__(self):
        self.stack = []
        self.min = None
        self.topv = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min  or val < self.min:
            self.min = min(self.stack) #val variable threw error
        self.topv = val

    def pop(self) -> None:
        if self.min == self.topv:
            self.stack.pop()
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = None
        else:
            self.stack.pop()
        if self.stack:
            self.topv = self.stack[-1]
            
    def top(self) -> int:
        return self.topv

    def getMin(self) -> int:
        return self.min
 
