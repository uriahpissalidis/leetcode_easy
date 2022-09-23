class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s)-1
        while i<j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return s

        #for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]
