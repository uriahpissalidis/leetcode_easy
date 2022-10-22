class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        out = set()
        for i in range(1, len(nums)):
            if nums[i-1]+nums[i] in out:
                return True
            out.add(nums[i-1]+nums[i])
            print(out)
        return False