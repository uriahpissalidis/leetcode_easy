class Solution:
    def countAsterisks(self, s: str) -> int:
        output, divCount = 0, 0
        
        for char in s:
            if char == '|':
                divCount += 1
            elif char == '*' and divCount % 2 == 0:
                output += 1
                
        return output