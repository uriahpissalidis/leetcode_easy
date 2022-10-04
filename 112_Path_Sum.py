class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        # solution 1
        if root is None:
            return False # edge case
        
        def dfs(root, curr_sum):
            if root.left is None and root.right is None:
                return curr_sum - root.val == 0 #reset if at leaf
            
            if root.left: #left traversal
                left_subtree = dfs(root.left, curr_sum - root.val)
            else:
                left_subtree = False
            
            if root.right: #right traversal
                right_subtree = dfs(root.right, curr_sum - root.val)
            else:
                right_subtree = False
            
            return left_subtree or right_subtree
        
        return dfs(root, targetSum)
    
        # solution 2
        if root is None:
            return False
        
        return self.traverse(root, targetSum)
    
        def traverse(self, root, target):
            target -= root.val

            if not root.left and not root.right:
                if target == 0:
                    return True
                return False

            if root.left:
                if self.traverse(root.left, target):
                    return True
            if root.right:
                if self.traverse(root.right, target):
                    return True

            return False