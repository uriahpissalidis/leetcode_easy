class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # solution 1
        return haystack.find(needle)
    
        # solution 2
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
