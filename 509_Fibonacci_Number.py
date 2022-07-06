class Solution:
    def fib(self, n: int) -> int:
        # method 1, via Binet's Formula
        sqrt5 = math.sqrt(5)
        return int((( (1 + sqrt5) ** n - (1 - sqrt5) ** n ) / ( 2 ** n * sqrt5 )))