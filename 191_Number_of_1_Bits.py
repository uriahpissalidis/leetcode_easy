class Solution:
    def hammingWeight(self, n: int) -> int: 
        # O(n) runtime, O(1) space
        ans = 0
        while n:
            n &= (n-1) # removes the rightmost bit
            ans += 1
        return ans
        
        # O(n) runtime, O(1) space
        ans = 0
        while (n != 0):
            ans = ans + (n & 1) # removes the rightmost bit
            n = n >> 1
        return ans
    
        return str(bin(n)).count("1")
