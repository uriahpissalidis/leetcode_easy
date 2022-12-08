class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(set(c.values())) == len(set(c.keys()))
        
        # 2nd, faster solution
        c = Counter(arr)
        x = []
        for k,v in c.items():
            if v in x:
                x.append(v)
                return False
            x.append(v)
        
        return True
