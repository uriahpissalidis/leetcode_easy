class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1: return 0
        return n if n%2 else n//2

        """
        if n == 1:
            return 0
        if n & 1:
            return n 
        return n// 2
        """