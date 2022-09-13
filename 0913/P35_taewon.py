'''
최단거리 경우의수 공식
(m+n)! / m!*n!
'''

import math

class Solution:
    def uniquePaths(self, m: int, n: int):
        return int(math.factorial(m+n-2)/(math.factorial(m-1) * math.factorial(n-1)))