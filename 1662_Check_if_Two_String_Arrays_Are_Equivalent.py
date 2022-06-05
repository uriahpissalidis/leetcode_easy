class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        k=''.join(word1)
        l=''.join(word2)
        if k==l:
            return True
        else:
            return False