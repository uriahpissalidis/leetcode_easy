class Solution:
    def middleNode(self, head):
        # two loops, O(2n) runtime, O(1) space complexity
        count, curr = 0, head
        while curr:
            count += 1
            curr = curr.next
        curr = head
        count = count//2
        while count != 0:
            count -= 1
            curr = curr.next
        return curr
        
        # one loop solution, O(n) runtime, O(1) space complexity
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow