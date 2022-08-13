class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = len(nums)
        for i, v in enumerate(nums):
            if v == val:
                counter -= 1
                nums[i] = -1
        nums.sort(reverse=True)
        return counter