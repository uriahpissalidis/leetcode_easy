from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        
        # idea is to count odd occurrences of letters
        oddCount = set()
        for letter in s:
            if letter not in oddCount:
                oddCount.add(letter)
            else:
                oddCount.remove(letter)
        if len(oddCount) != 0:
            return len(s) - len(oddCount) + 1
        else:
            return len(s)
        
        # same idea but faster
        freqs = Counter(s)
        res = 0
        for freq in freqs.values():
            if not res % 2 and freq % 2:
                res += 1
            res += (freq - freq % 2)
        return res