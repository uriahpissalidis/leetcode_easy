class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []
        for ch in S:
            # upon seeing two matching characters, pop the stack
            if output and ch == output[-1]: 
                output.pop()
            # otherwise they join
            else: 
                output.append(ch)
        # join the output stack at the end to form the stringa
        return ''.join(output)

        """
        # TLE on leetcode
    
    def solution(s):
        # edge case of str length 1
        if len(s) == 1: return s
        num, ans, i = 0, s, 0
        
        while i != len(ans)-1:
            if ans == "": return ""
            if ans[i] == ans[i+1]:
                ans = ans[:i] + ans[i+2:]
                i = 0
            else:
                i += 1
        return ans
        """