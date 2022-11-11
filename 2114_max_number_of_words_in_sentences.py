# 2114 Maximum Number of Words Found in Sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        # most recent solution
        # TC: O(N) || SC: O(1)
        ans = 0
        for i in range(len(s)):
            s[i] = s[i].count(' ') + 1
            ans = max(ans, s[i])
        return ans

        
        """
        I think the idea is to go through each set of quotes
        then count the number of spaces
        keep a global max
        in the for loop iterate via char, count num of spaces with a local var
        """
        maxWords = 0
        localCount = 0
        for sentenceNumber in sentences:
            localCount = len(sentenceNumber.split())
            if localCount >= maxWords:
                maxWords = localCount
        return maxWords
