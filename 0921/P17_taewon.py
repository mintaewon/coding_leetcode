class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def func(p,q):
            if (p==None) and (q==None):
                return True
            if p and q and (p.val == q.val):
                return func(p.left, q.left) and func(p.right, q.right)
            return False
        
        if func(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)