class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Runtime: O(n)
        Space:   O(n)
        """
        # bear in mind, strings are immutable
        if len(s) == 1: return s #edge case
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} #vowels
        s, i, j = list(s), 0, len(s)-1 #s to list and two pointers
        while i < j:
            if s[i] in v and s[j] in v: #if vowels, swap
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
            if s[j] not in v: #move left
                j-=1
            if s[i] not in v: #move right
                i+=1
        return "".join(s) #return the result in a string
    
    """
    2nd solution
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0: return s
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack, s = [], list(s) #stack
        for char in s:
            if char in v:
                stack.append(char)
        for i in range(0, len(s)):
            if s[i] in v:
                s[i] = stack.pop(len(stack)-1)
        return "".join(s)
    """