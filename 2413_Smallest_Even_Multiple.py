class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1) #solution 1
        
        if n%2 != 0: #solution 2
            return n*2
        return n
