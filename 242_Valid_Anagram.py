# second solution, more recent
# Runtime: O(n)
# Memory: O(n) because of the counter
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = Counter(s)
        for letter in t:
            if letter in d:
                d[letter] -= 1
        for key in d:
            if d[key] != 0:
                return False
        return True

"""
Another solution
# Runtime: O(n)
# Memory: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
"""
