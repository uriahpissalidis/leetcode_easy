class Solution:
def unequalTriplets(self, nums: List[int]) -> int:
    if len(nums) < 3: return 0
    ans = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                    ans += 1
    return ans
