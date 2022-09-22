class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s, count = sorted(heights), 0
        for i in range(len(heights)):
            if s[i] != heights[i]:
                count += 1
        return count