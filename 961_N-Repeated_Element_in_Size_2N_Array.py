from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
        n = len(nums)//2 + 1
        for num in nums:
            if nums.count(num) == n-1:
                return num
        """
        """
        n = len(nums)//2 + 1
        x = Counter(nums)
        for num in nums:
            if x[num] == n-1:
                return num
        """