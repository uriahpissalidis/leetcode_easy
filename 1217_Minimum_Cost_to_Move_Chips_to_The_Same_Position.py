class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ce = co = 0
        for i in range(len(position)):
            if position[i]%2:
                co+=1
            else:
                ce+=1
        return min(co, ce)
