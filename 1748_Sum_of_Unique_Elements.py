class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        occurrence = {item: nums.count(item) for item in nums}
        for i in occurrence:
            if occurrence.get(i) == 1:
                ans += i
        return ans