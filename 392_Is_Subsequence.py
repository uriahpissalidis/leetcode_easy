class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, k = 0, 0, ''
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                k += s[i]
                i+=1 #iterate if found
            j+=1 #move the pointer on string t
        if k == s:
            return True
        else:
            return False