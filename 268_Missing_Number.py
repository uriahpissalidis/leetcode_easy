class Solution(object):
    def missingNumber(self, nums):
        #print, indices - sum of nodes
        return sum(range(len(nums)+1)) - sum(nums)