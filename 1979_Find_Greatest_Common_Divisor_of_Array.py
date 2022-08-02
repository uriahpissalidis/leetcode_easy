class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        small, large = nums[0], nums[-1]
        for i in range(small, 0, -1):
            if small%i==0 and large%i==0:
                return i