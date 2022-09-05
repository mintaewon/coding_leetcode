class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2 : 
            return  2
        pre_step=1
        temp=0
        curr=1
        for i in range(1,n):
            temp = curr
            curr = curr + pre_step
            pre_step = temp
        return curr


solver = Solution()
n=4
print(solver.climbStairs(n))
        