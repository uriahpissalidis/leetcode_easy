class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        mx = (-1,-1)
        lst = 0
        for i in range(len(logs)):
            mx = max(mx, (logs[i][1] - lst, -logs[i][0]))
            lst = logs[i][1]
        
        return -mx[1]