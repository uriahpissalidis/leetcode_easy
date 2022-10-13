class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # SC O(n) || TC O(n)
        s = set()
        for num in nums:
            if num != 0:
                s.add(num)
        return len(s)