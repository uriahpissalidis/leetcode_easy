class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        #if len(nums)<4: 
        nums.sort()
        pair1 = nums[-1] * nums[-2]
        pair2 = nums[0] * nums[1]
        return pair1 - pair2