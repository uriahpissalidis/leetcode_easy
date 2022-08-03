class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ans = {}
        for c in s:
            if c not in ans:
                ans[c] = s.count(c)
        comp = s.count(s[0])
        for num in ans:
            if ans[num] != comp: return False
        return True