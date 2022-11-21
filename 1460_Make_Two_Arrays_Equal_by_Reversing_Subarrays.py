class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = Counter(target)
        for num in arr:
            if num in d:
                d[num] -= 1
        for v in d.values():
            if v != 0:
                return False
        return True
