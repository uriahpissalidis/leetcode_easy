class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        # way one
        xor = x ^ y
        ham = 0
        while xor != 0:
            ham += xor % 2
            xor >>= 1
        return ham

        # way two
        x, y = x ^ y, 0
        while x:
            y += 1
            x = x & (x - 1)
        return y