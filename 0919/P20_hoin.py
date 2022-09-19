class Solution:
    def productExceptSelf(self, nums):
        st = [1 for _ in range(len(nums))]
        N = len(nums)
        left=nums[0]
        
        for i in range(1,N-1):
            st[i]*=left
            left *= nums[i]
        
        right=nums[-1]
        for j in range(N-2,0,-1):
            st[j]*=right
            right *= nums[j]
        st[-1] = left
        st[0] = right
            
        return st

nums=[-1,2,3,4] # 24, 12, 8, 6
solver = Solution()
print(solver.productExceptSelf(nums))

