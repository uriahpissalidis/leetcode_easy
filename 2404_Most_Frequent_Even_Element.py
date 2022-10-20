class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        l=[]
        for i in nums:
            if i%2 == 0:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        if len(d)==0:
            return -1
        else:
            t = max(d.values())
            for k,v in d.items():
                if v == t:
                    l.append(k)
            return min(l)
