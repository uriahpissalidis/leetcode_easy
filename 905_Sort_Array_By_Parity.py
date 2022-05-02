class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """i = 0
        j = len(nums)-1
        "i even, j even, i odd j even, i even j odd, i odd j odd"
        while i != j:
            if nums[i]%2 == 0 and nums[j]%2 == 0:
                j -= 1
            elif nums[i]
        """
        # Naive solution
        odd = []
        even = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        while odd:
            even.append(odd.pop())
        return even