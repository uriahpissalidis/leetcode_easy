class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        # 1-line solution
        # return num == 0 or num%10 != 0

        # naive solution, converting the num to a string
        strNum = str(num)
        if len(strNum) == 1: return True
        if strNum[-1] == '0': return False
        else: return True