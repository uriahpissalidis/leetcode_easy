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
    
        # NO bit manipulation solution
        # this step is for padding 0's
        longer = len(bin(y))-2
        if x > y: longer = len(bin(x))-2
            
        # turn both to binary, count 1's in binary representation within count
        x, y, count = format(x, '0b').zfill(longer), format(y, '0b').zfill(longer), 0 
        for i in range(len(x)):
            if x[i] != y[i]: count += 1
        return count
