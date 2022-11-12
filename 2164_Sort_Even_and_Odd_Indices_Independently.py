class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # recognize that odd numbers go in odd indices, in non-increasing order
        # while even numbers go in even indices, in increasing order
        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2], reverse=True)
        return nums