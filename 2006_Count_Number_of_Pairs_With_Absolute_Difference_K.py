class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:        
        seen, pairCount = {}, 0
        
        # fill the set
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        # find the complement to find number of pairs
        for num in nums:
            if num+k in seen:
                pairCount += seen[num + k]
        return pairCount