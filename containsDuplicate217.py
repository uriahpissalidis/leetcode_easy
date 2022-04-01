# leetcode: 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() #utilizing a set to find a duplicate
        for n in nums:
            if n in seen:
                return True #if it is seen, return true
            else:
                seen.add(n) #otherwise add in the set
        return False