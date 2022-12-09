class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        curr = 0
        ans = []
        
        for i in range(len(nums)):
            curr += nums[i]
            total -= nums[i]
            ans.append(nums[i])
            if curr > total:
                return ans
