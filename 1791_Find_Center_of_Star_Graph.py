class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # the idea is to find the most repeated number
        # center will always have the most repeated connections
        sol = []
        
        # push all edges into a list
        for i in range(len(edges)):
            for j in range(len(edges[0])):
                sol.append(edges[i][j])
                
        # count the number of occurences, return when found
        for num in sol:
            if sol.count(num) > 1:
                return num