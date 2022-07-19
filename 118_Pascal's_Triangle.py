class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # edge cases
        if numRows == 0: return [[]]
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        ans = [[1], [1,1]]

        # constructing rows beyond 2
        count = 2
        while count < numRows:
            count += 1
            temp = [None]*count
            start, end = 0, len(temp)-1
            temp[start] = 1
            temp[end] = 1
            print(temp)
            while start != end:
                start += 1
                if start == end:
                    break
                temp[start] = ans[count-2][start-1] + ans[count-2][start]
            ans.append(temp)
        return ans