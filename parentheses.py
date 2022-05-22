#!/usr/bin/env python3

#leetcode fun
#Need to add function to watch for proper structure use 
#Last open bracket needs to see matching close or another open
#If proper closeing bracket is returned the preceding open bracket is taken into account
class Solution:
  def isValid(self, s: str) -> bool:
        self.leftside = ["[", "{", "("]
        self.rightside = ["]", "}", ")"]
        self.pdict = {"(":0, "[":0, "{":0}
        self.status = True
        while self.status:
            for p in s:
                if p in self.leftside:
                    self.pdict[p] +=1
                else:
                    pkey = self.leftside[self.rightside.index(p)]
                    if self.pdict[pkey] > 0:
                        self.pdict[pkey] -= 1
                    else:
                        self.status = False
            break
        return self.status
