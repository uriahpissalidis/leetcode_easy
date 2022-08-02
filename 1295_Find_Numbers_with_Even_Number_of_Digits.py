class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                ans += 1
        return ans

    """
    # slower but no str casting
    def findNumbers(self, nums: List[int]) -> int:
        def length_calculator(num):
            counter = 0   # Counter 
            num = abs(num)
            while(num):         
                counter = counter + 1
                num = int(num/10)
            return counter
        count = 0
        for num in nums:
            x = length_calculator(num) 
            if x%2==0: count += 1
        return count
    """