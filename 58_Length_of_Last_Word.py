class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for letter in s.rstrip(" ")[::-1]:
            if letter==" ":
                break
            count+=1
        return count