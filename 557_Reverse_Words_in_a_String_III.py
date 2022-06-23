class Solution:
    def reverseWords(self, s: str) -> str:
        ans, words = "", s.split(" ")
        for word in words:
            word = word[::-1]
            ans = ans + word + " "
        return ans[:-1]