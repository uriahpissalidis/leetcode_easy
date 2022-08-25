class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (len(ransomNote) == 1 and len(magazine) == 1) and ransomNote != magazine:
            return False
        if len(ransomNote) > len(magazine):
            return False
        d = {}
        for c in magazine:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in ransomNote:
            if c in d:
                d[c] -= 1
                if d[c] == -1:
                    return False
            if c not in d:
                return False
        return True