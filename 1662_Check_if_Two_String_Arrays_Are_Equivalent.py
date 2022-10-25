class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        k=''.join(word1)
        l=''.join(word2)
        if k==l:
            return True
        else:
            return False
        
        # cleaner solution
        return "".join(word1)=="".join(word2)
        
        # lengthier, utilizing string concatenation
        piece1, piece2 = '', ''
        for piece in word1:
            piece1 += piece
        for piece in word2:
            piece2 += piece
        
        if piece1 == piece2:
            return True
        return False
