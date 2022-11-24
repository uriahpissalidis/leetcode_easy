class Solution:
    def findFinalValue(self, nums: List[int], o: int) -> int:
        # No extra space
        while o in nums:
            if o in nums:
                o=o*2
        return o
        
        # initial solution
        d = set(nums)
        while o in d:
            o *= 2
        return o