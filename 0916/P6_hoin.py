class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = set(range(n+1)) - set(nums)
        return int(list(a)[0])