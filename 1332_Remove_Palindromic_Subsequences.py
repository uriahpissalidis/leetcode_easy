class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # since there are only two characters
        # and the characters don't have to be continguous
        # intution says answer can only be 1 or 2, since you can group
        # the a's, then the b's and be done
        # s.reversed() == [::-1]
        if s[::-1] == s: return 1
        else: return 2