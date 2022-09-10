class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # O(n) runtime
        # O(1) space complexity
        if len(nums)==1: return nums #edge case
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i]%2==0:
                i+=1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
        return nums
        
        """
        # 2nd way
        # O(n) runtime
        # O(n) space complexity
        def sortArrayByParity(self, nums: List[int]) -> List[int]:
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
        """