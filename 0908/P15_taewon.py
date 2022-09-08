class Solution:    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 노드가 없을때 0 반환
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1