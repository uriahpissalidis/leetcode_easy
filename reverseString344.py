# Python submissions for Leetcode: 344. Reverse String, in array, in-place
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0 #left pointer
        j = len(s)-1 # "0-indexed"
        while i < j:
            s[i], s[j] = s[j], s[i] # implicit tuple would return the same as an explicit tuple
            i, j = i+1, j-1 #+1 to the i (our left var) and -1 to the j (our right var)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]
        