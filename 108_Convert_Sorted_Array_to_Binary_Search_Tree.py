class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createBST(nums, low, high):
            if low > high:
                return None
            mid = (high + low)//2
            root = TreeNode(nums[mid])
            root.left = createBST(nums, low, mid-1)
            root.right = createBST(nums, mid + 1, high)
            return root
        return createBST(nums, 0, len(nums)-1)