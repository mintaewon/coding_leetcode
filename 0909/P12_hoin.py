from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str):
        if Counter(s)==Counter(t):
            return True
        else:
            return False
            
solver=Solution()
s = "aacc"
t = "ccac"
print(solver.isAnagram(s,t))
