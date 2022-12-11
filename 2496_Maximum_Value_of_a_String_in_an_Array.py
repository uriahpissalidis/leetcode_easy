class Solution:
    def maximumValue(self, s: List[str]) -> int:
        ans = 0
        for x in s:
            if all([y.isnumeric() for y in x]):
                ans = max(ans, int(x))
            else:
                ans = max(ans, len(x))   
        return ans
