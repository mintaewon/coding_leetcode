# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math
class Solution:
    def levelOrder(self, root):
        d = deque(root)
        result=[]
        k = math.ceil(math.log2(len(root)+1))        
        for i in range(k):
            curr=[]
            for _ in range(2**i):
                try : 
                    curr.append(d.popleft())
                except : 
                    break
            result.append(curr)
        
        return result
solver = Solution()
# root = [3,9,20,'a','a',15,7,5]
root=[1]
solver.levelOrder(root)   


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    que = collections.deque([root])
    if not root:
        return []
    while que:
        level = []
        for i in range(0,len(que)):
            curr = que.popleft()
            level.append(curr.val)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        result.append(level)
    return result