class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        fs = s.find('6')
        if fs >= 0:
            return int(s[:fs] + '9' + s[fs+1:])
        return num