'''
None 을 한번에 처리할 수 있는 방법이 생각나지 않음
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        if root.left and root.right:
            root.left, root.right = root.right, root.left
            self.invertTree(root.right)
            self.invertTree(root.left)

        elif root.left and not root.right:
            root.left, root.right = None, root.left
            self.invertTree(root.right)

        elif not root.left and root.right:
            root.left, root.right = root.right, None
            self.invertTree(root.left)
            
        return root