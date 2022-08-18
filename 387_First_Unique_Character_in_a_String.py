class Solution:
    def firstUniqChar(self, s: str) -> int:
        # optimized solution
        d = {}
        for l in s:
            if l not in d: d[l] = 1
            else: d[l] += 1
        
        index = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break
        
        return index
        
        # naive solution
        """
        count = 0
        for c in s:
            if s.count(c) == 1:
                return count
            count += 1
        return -1
        """