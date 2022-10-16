class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d, ans = {}, 0
        for num in nums:
            if num > 0: # store positive numbers
                d[num] = 0
        for num in nums:
            if num < 0 and abs(num) in d: # less than 0 and positive num exists in dictionary
                d[abs(num)] = num
        for key in d:
            if d[key] + key == 0:
                ans = max(key, ans)
        if ans == 0:
            return -1
        else:
            return ans