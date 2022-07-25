class Solution:
    def repeatedCharacter(self, st: str) -> str:
        s = set()
        for x in st:
            if x in s:
                return x
            else:
                s.add(x)