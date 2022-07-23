class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # edge case
        if len(word) == 1: return word
        idx = word.find(ch)        
        if idx:
            return word[:idx+1][::-1] + word[idx+1:]
        return word