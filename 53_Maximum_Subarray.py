
"""
class Solution:
    def maxSubArray(self, A):
        
        # Basically, you're starting a new run of numbers if the previous sum is negative. 
        # And the maxSum = max(maxSum, curSum) gets you the maximum sum out of all the current ones.
        
        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
        return maxSum
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        tempSum = 0 
        
        for num in nums:
            tempSum += num
            if tempSum > maxSum:
                maxSum = tempSum
                
            if tempSum < 0:
                tempSum = 0
                
        return maxSum

