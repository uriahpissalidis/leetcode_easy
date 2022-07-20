class Solution:
    def generateTheString(self, n: int) -> str:
        is_odd = n % 2 == 1
        if is_odd:
            return 'a' * n
        else:
            return 'a' * (n - 1) + 'b'