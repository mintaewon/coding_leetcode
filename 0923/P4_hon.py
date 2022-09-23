class Solution:
    def hammingWeight(self, n: int) -> int:
        S=bin(n)
        return S.count('1')
        