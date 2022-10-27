class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def solve(s,target):
                l,h=0,len(s)-1
                ans=-1
                while l<=h:
                    mid=(l+h)//2
                    if s[mid]==target:
                        return mid+1
                    elif s[mid]>target:
                        ans=mid
                        h=mid-1
                    else:
                        l=mid+1
                return len(s) if ans==-1 else ans

        s=[]
        nums.sort()
        #calculating cumulative sum of sorted array
        s.append(nums[0])
        for i in range(1,len(nums)):
            s.append(nums[i]+s[-1])

        res=[]
        for i in range(len(queries)):
            res.append(solve(s,queries[i]))
        return res
