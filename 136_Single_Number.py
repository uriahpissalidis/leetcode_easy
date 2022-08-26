class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Runtime: O(n) | Memory:  O(1)
        nums.sort()
        # if odd len and unique still not found, return the last number
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i] # unique num will be here
        return nums[-1] # or at the end for cases of odd length