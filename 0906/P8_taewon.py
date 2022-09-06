''''
피보나치 수열
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        start,end = 1,2
        for _ in range(n-1):
            start,end = end, start+end
        return start