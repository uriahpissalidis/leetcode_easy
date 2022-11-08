class Solution:
    def checkString(self, s: str) -> bool:
        # ascii difference solution
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) < 0:
                return  False
        return True
    
        # "switch" solution
        found_b = False
        for c in s:
            if c == "a" and found_b:
                return False
            elif c == "b":
                found_b = True
        return True
        
        # index and list slicing solution
        # try:
        #     b = s.index('b')
        # except ValueError:
        #     return True
        # try:
        #     if s[b:].index('a') == -1: return True
        # except ValueError:
        #     return True
        # return False