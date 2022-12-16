class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        dic = {}
        
        for i in arr:
            if bin(i)[2:].count('1') not in dic:
                dic[bin(i)[2:].count('1')] = [i]
            
            else:
                dic[bin(i)[2:].count('1')].append(i)
                
        lis = []
        for i in sorted(dic):
            lis.append(sorted(dic[i]))
            
        return sum(lis , [])
