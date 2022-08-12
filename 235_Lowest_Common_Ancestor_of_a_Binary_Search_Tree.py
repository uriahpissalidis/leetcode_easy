class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        while(True):
            if ((current.val - p.val )*( current.val - q.val) <= 0):
                return current
            if current.val > p.val:
                current = current.left
            else:
                current = current.right