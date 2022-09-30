class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # Runtime: O(n)
        # Space:   O(1)
        ans = 0
        for word in words:
            if s.startswith(word):
                ans += 1
        return ans