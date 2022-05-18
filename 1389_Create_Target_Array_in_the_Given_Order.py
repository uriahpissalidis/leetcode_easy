class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        # I feel like this is cheating but it is the 
        # solution that naturally arrived to me
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target
            