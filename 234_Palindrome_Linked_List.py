class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        # find the middle of the list with slow ptr
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second half of the list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        # verify if palindrome (prev holds last node)
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True