class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        sol = []
        for r in range(len(matrix[0])):
            temp = []
            for c in range(len(matrix)):
                temp.append(matrix[c][r])
            sol.append(temp)
            
        return sol