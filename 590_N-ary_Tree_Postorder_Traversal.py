class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None: return res
        def rec(root, res):
            for child in root.children:
                rec(child, res)
            res.append(root.val)
        rec(root, res)
        return res