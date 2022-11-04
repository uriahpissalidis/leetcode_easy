class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for num in d:
            if d[num]%2:
                return False
        return True