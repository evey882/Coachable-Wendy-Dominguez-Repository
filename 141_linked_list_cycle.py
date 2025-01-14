"""141. Linked List Cycle"""

from typing import List

class Solution:
    """Solution Class"""
    def hasCycle(self, head) -> bool:
        """
            This function determines whether there is a cycle in a passed in linked list.
            It does so by changing the value inside the node to something out of range, if
            this value is encountered again then it is safe to say that there is in fact
            a cycle. This is completed in O(N) time with O(1) space.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
