class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        # This is a simple binary search
        left = 0
        right = len(nums)-1
        
        # Cut the array in half
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left