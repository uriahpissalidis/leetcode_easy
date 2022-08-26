class Solution:
    def climbStairs(self, n: int) -> int:
        n+=1
        root5 = math.sqrt(5)
        result = int((( (1 + root5) ** n - (1 - root5) ** n ) / ( 2 ** n * root5 )))
        return result
        