class Solution:
    def countBits(self, n: int) -> List[int]:
        # two cases
        # if number is odd, number // 2 + one extra zero
        # 0101 -> 5
        # 0010 -> 2
        
        # if number is even, same number of ones
        # 0100 -> 4
        # 0010 -> 2
        result = [0] * (n + 1)
        for i in range(n + 1):
            num_of_ones = 0
            if i & 1:
                num_of_ones = result[i // 2] + 1
            else:
                num_of_ones = result[i // 2]
            result[i] = num_of_ones
        
        return result