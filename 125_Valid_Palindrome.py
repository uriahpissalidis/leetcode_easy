class Solution:
    def isPalindrome(self, s: str) -> bool:
        # edge case for empty string returns true
        if s == '' or s == ' ': return True
        s, count = s.lower(), 0
        ans = [None]*len(s)
        for char in s:
            if (ord(char) >= 97 and ord(char) <= 122) or char.isdigit():
                ans[count] = char
                count+=1
        ans = ans[0:count]
        l, r, mid = 0, len(ans)-1, len(ans)//2
        while l != mid:
            if ans[l] != ans[r]:
                return False
            l+=1
            r-=1
        return True
        """
        if ans == ans[::-1]: 
            return True
        else:
            return False
        """