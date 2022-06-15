from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # edge cases
        if len(s) == 0: return True
        if len(s)%2 == 1: return False
        
        # deque is slightly faster than a list
        d = deque()
        for char in s:
            if char == '{' or char == '[' or char == '(':
                d.append(char)
            if char == ')':
                if len(d) > 0 and d[-1] == '(':
                    d.pop()
                else:
                    return False
            if char == ']':
                if len(d) > 0 and d[-1] == '[':
                    d.pop()
                else:
                    return False
            if char == '}':
                if len(d) > 0 and d[-1] == '{':
                    d.pop()
                else:
                    return False
        if len(d) == 0: return True
        return False