class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        # Solution 1
        n = len(operations)
        total = 0
        for i in range(n):
            if operations[i] == '++X' or operations[i] == 'X++':
                total += 1
            else:
                total -= 1
        return total
        """
        """
        # Solution 2
        op_dict = {"--X" : -1, "X--" : -1,
                 "++X" : 1, "X++" : 1}
        return sum(op_dict[op] for op in operations)
        """
        """
        # Solution 3
        total = 0
        for addOrSub in operations:
            if addOrSub[1] == '+':
                total += 1
            else:
                total -= 1
        return total
        """