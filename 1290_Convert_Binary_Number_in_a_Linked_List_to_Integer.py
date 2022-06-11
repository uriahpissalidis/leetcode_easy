class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        data = ''
        
        while head is not None:
            data += str(head.val)
            head = head.next
            
        return int(data,2)