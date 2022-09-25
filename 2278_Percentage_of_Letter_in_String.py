class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return (s.count(letter) * 100 // len(s)) 
        """
        solution below taken from:
        https://leetcode.com/problems/percentage-of-letter-in-string/discuss/2100099/Easy-Python-Solution

        return ("%d" %(s.count(letter)/len(s)*100))
        """