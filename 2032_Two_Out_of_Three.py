class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d, d2, d3 = set(nums1), set(nums2), set(nums3)
        ans = set(list(d & d2) + list(d & d3) + list(d2 & d3))
        return list(ans)