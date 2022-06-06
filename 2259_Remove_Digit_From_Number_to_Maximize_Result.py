class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        final = 0
        for index,i in enumerate(number):
            if i == digit:
                res = number[:index] + number[index+1:]
                final = max(final, int(res))
        return str(final)