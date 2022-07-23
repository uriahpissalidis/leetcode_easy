class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # sort the array, as stated in the question
        nums.sort()
        
        # store the found indices, create a list the 
        # length of the found target with count function
        ans, count = [None]*nums.count(target), 0
        
        # iterate through and find the target indices
        for i in range(len(nums)):
            if nums[i] == target:
                ans[count] = i
                count += 1
            
            # if criteria are met return the answer
            if count == len(ans): 
                return ans
        return ans

"""
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        found = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                found.append(i)
                
                
        return found 
"""