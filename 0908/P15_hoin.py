class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def fromlist(values):
    def create(it):
        value = next(it)
        return None if value is None else TreeNode(value)
        
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    nextlevel = [root]
    try:
        while nextlevel:
            level = nextlevel
            nextlevel = []
            for node in level:
                if node:
                    node.left = create(it)
                    node.right = create(it)
                    nextlevel += [node.left, node.right]
        
    except StopIteration:
        return root
    raise ValueError("Invalid list")

from collections import deque
import math
class Solution:
    def levelOrder(self, root):
        que = deque([root])
        if not root:
            return 0
        level=0
        while que:
            for i in range(0,len(que)):
                curr = que.popleft()
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            level+=1
        return level


root = [3,9,20,None,None,15,7]
root = fromlist(root)
solver = Solution()
ans = solver.levelOrder(root)
print(ans)


