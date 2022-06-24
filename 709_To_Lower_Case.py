class Solution:
    def toLowerCase(self, s: str) -> str:
        # there's a reason this question has a ton of dislikes on it
        count, ans = 0, [""]*len(s)
        for char in s:
            if ord(char) >= 65 and ord(char) <= 90:
                converted = chr(ord(char)+32)
                ans[count] = converted
                count += 1
            else:
                ans[count] = char
                count += 1
        return(''.join(ans))