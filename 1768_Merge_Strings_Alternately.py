class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # optimized
        result = []
        for i in range(min(len(word1),len(word2))):
            result.append(word1[i] + word2[i])
            
        return ''.join(result) + word1[i+1:] + word2[i+1:]
        
        # naive, first solution
        """
        ans = [None]*(len(word1) + len(word2))
        idx=min(len(word1), len(word2))
        ansIndex, wordIndex = 0, 0
        while wordIndex != idx:
            ans[ansIndex] = word1[wordIndex]
            ans[ansIndex+1] = word2[wordIndex]
            ansIndex+=2
            wordIndex+=1
        if len(word1) == len(word2):
            return ''.join(ans)
        if len(word1) > len(word2):
            while wordIndex != len(word1):
                ans[ansIndex] = word1[wordIndex]
                ansIndex += 1
                wordIndex += 1
            return ''.join(ans)
        if len(word1) < len(word2):
            while wordIndex != len(word2):
                ans[ansIndex] = word2[wordIndex]
                ansIndex += 1
                wordIndex += 1
            return ''.join(ans)
        """