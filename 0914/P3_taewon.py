from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if sorted(Counter(nums).values(), reverse=True)[0] == 1:
            return False
        else:
            return True