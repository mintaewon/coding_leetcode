class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(nums)!=len(list(numset)):
            return True
        else :
            False
        