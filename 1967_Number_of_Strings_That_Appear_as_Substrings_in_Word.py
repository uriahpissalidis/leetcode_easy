# faster solution
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt=0
        for x in patterns:
            if x in word:
                cnt+=1
        return cnt

# initial solution
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count, x = 0, word
        for i in range(len(patterns)):
            if x.count(patterns[i]):
                count += 1
        return count