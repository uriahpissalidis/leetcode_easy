class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # edge cases
        if n == 0:
            return False
        if n == 1:
            return True
        x = 3
        while(x != n):
            x *= 3
            if(x > n):
                return False
        return True